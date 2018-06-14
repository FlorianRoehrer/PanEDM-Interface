#Standard modules
import sys
import time
import datetime

#GUI class created by QtDesigner
from GUI.PanEDMInterface_Main_Window_GUI import *

#Modules for functionality
from Infowindow import *
from Login import *
from Settings import *
from Modules.Timer import *
from Modules.TerminalOutput import *
from Modules.read_write_files import *
from Modules.Marker import *
from Modules.comm_write_worker import *

#__________________________________________________________________________________

#Main Window class. It inherits from the GUI class and adds the functionality
class PanEDM_Interface(QtWidgets.QMainWindow,Ui_PanEDMInterfaceMain):
    def __init__(self, **kwargs):
        super(PanEDM_Interface, self).__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        #Reroute the terminal output to the GUI
        self.rerouteTerminalOutput()
        
        #Elements to hide
        self.switchlist.hide()
        
        #Buttons deactivated at program start
        self.autoPauseButton.setEnabled(False)
        self.autoOnestepButton.setEnabled(False)
        self.autoStopButton.setEnabled(False)
        self.autoStartButton.setEnabled(False)
        
        #Class variable definitions
        self.clockVar         = 0
        self.activeLineVar    = 0
        self.stepInterval     = 10 #msec
        self.runActive        = False
        self.firstLogin       = True
        self.dev_file         = './config/dev_paths.txt'
        self.logFilePath      = './Logs/'
        
        #Set the actual run number
        self.checkRunNumber()
        self.run_number      += 1
        self.runnumber.setText('#' + str(self.run_number))
        
        #Connect Buttons to methods
        self.autoStartButton.clicked.connect(self.startButtonFunc)
        self.autoStopButton.clicked.connect(self.stopButtonFunc)
        self.autoPauseButton.clicked.connect(self.pauseButtonFunc)
        self.autoOnestepButton.clicked.connect(self.onestepButtonFunc)
        self.autoChooseButton.clicked.connect(self.choose_macro_file)
        self.autoLoadButton.clicked.connect(self.load_macro_file)
        
        #Connect actions (Menus and toolbars)
        self.actionClose.triggered.connect(self.close_application)
        self.actionChange_user.triggered.connect(self.UserLogin)
        self.actionAbout.triggered.connect(self.about)
        self.actionSettings.triggered.connect(self.Settings)
        
        #Run clock timer instance. It is started by invoking self.runTimer.start_loop(1000)
        #Stop with self.runTimer.stop_loop()
        self.runTimer = function_timer()
        self.runTimer.executeSignal.connect(self.clockIncrement)
        
        #Color definitions for the run status text and the class instance for the colorization
        self.activeColor      = QtGui.QColor(0, 85, 255)
        self.finishedColor    = QtGui.QColor(0, 255, 0)
        self.ColoringActive   = ColorMarker(self.runStatusTextEdit, self.activeColor)
        self.ColoringFinished = ColorMarker(self.runStatusTextEdit, self.finishedColor)
        
        #File handler instance. This is used to read and write all the ASCII files. self.filehandler.loadmacro(macrofile)
        self.filehandler = read_write_files()
        
        #Adjust the tab stop width of the run status section to have the text in accurate columns
        #self.runStatusTextEdit.setTabStopWidth(140)
        #self.runStatusTextEdit.setTabStopWidth(320)
        self.runStatusTextEdit.autoFormatting()
        
        #Set the user at the start of the application
        self.UserLogin()
        
    #Check the last run number
    def checkRunNumber(self):
        file = open('./config/run_number.txt', 'r')
        self.run_number = int(file.readline())
        file.close()
        
    #This method starts the measurement run. It is started by pressing the start button.
    def startButtonFunc(self):
        self.runTimer.start_loop(1000)
        self.autoPauseButton.setEnabled(True)
        self.autoStopButton.setEnabled(True)
        self.autoStartButton.setEnabled(False)
        self.autoOnestepButton.setEnabled(False)
        self.ColoringActive.activate(self.activeLineVar)
        
        if self.runActive == False:
            self.newRun()
            
        self.macroTimer.start_loop(self.stepInterval)
        
    #This method switches to the next step in the macro file. It is invoked by the macro timer. The time between the steps is self.stepInterval    
    def macroNextStep(self):
        try:
            next(self.comm_write_worker.runInstance)
        except:
            self.stopButtonFunc()
            
    def newRun(self):
        #Command file writer thread
        self.comm_write_thread = QtCore.QThread(self)
        self.comm_write_worker = comm_write_worker(self.user, self.macrofile, self.timestamp(), str(self.run_number), self.dev_file)
        self.comm_write_worker.moveToThread(self.comm_write_thread)
        self.comm_write_worker.file_written.connect(self.markActiveLine)
        self.comm_write_worker.macro_finished.connect(self.stopButtonFunc)
        
        self.comm_write_worker.wait_signal.connect(self.wait)
        
        self.comm_write_thread.started.connect(self.comm_write_worker.startRun)
        self.comm_write_thread.start()
        self.macroTimer = function_timer()
        self.macroTimer.executeSignal.connect(self.macroNextStep)
        self.setRunActive()
        print(self.timestamp() + ' : Measurement run #' + str(self.run_number) + ' started!')
        
    def wait(self, timestring):
        self.macroTimer.wait(float(timestring)*1000)
        
    def setRunActive(self):
        self.runActive = True
        self.autoChooseButton.setEnabled(False)
        self.autoLoadButton.setEnabled(False)
        self.configFileLineEdit.setReadOnly(True)
        file = open('./config/run_status.txt', 'w')
        file.write('1')
        file.close()
        
    def unsetRunActive(self):
        self.runActive = False
        self.autoChooseButton.setEnabled(True)
        self.autoLoadButton.setEnabled(True)
        self.configFileLineEdit.setReadOnly(False)
        file = open('./config/run_status.txt', 'w')
        file.write('0')
        file.close()
        
    #This method is executed by pressing the stop button
    def stopButtonFunc(self):
        self.autoStopButton.setEnabled(False)
        self.autoStartButton.setEnabled(True)
        self.autoPauseButton.setEnabled(False)
        self.autoOnestepButton.setEnabled(True)
        self.autoStartButton.setText('Start run')
        
        self.runTimer.stop_loop()
        self.totalTime = self.clockVar
        self.clockVar = 0
        self.runClockValue.setText(str(datetime.timedelta(seconds=self.clockVar)))
        self.macroTimer.stop_loop()
        self.comm_write_thread.quit()
        self.unsetRunActive()
        self.ColoringFinished.activate(self.activeLineVar)
        self.activeLineVar = 0
        print(self.timestamp() + ' : Measurement run #' + str(self.run_number) + ' finished! The total run time was ' + str(datetime.timedelta(seconds = self.totalTime)))
        
        #Save the run number of the finished run
        file = open('./config/run_number.txt', 'w')
        file.write(str(self.run_number))
        file.close()
        
        self.run_number += 1
        self.runnumber.setText('#' + str(self.run_number))
        self.runStatusTextEdit.setText(self.statustext)
        self.ColoringActive.activate(0)
        
    #This method is executed by pressing the pause button
    def pauseButtonFunc(self):
        #self.runTimer.stop_loop()
        self.macroTimer.stop_loop()
        self.autoStartButton.setText('Resume')
        self.autoPauseButton.setEnabled(False)
        self.autoStartButton.setEnabled(True)
        self.autoStopButton.setEnabled(True)
        self.autoOnestepButton.setEnabled(True)
    
    #This method is executed by pressing the execute one step button
    def onestepButtonFunc(self):
        if self.runActive == False:
            self.newRun()
            self.runTimer.start_loop(1000)
            self.autoStartButton.setText('Resume')
        
        self.macroNextStep()
        self.autoStopButton.setEnabled(True)
    
    #This method marks the currently active line during the measurement run.
    def markActiveLine(self):
        self.activeLineVar += 1
        #print(self.activeLineVar)
        self.ColoringActive.activate(self.activeLineVar)
        if self.activeLineVar != 0:
            self.ColoringFinished.activate(self.activeLineVar-1)
            
    #This Method increments the run clock each time self.runTimer gives a signal.
    def clockIncrement(self):
        self.clockVar += 1
        self.runClockValue.setText(str(datetime.timedelta(seconds = self.clockVar)))
    
    
    def choose_macro_file(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Choose the macro file to load')
        self.configFileLineEdit.setText(path)
        
    def load_macro_file(self):
        path = self.configFileLineEdit.displayText()
        if path == '':
            errortitle = 'File path empty'
            errortext  = 'The file path is empty!'
            add_error  = 'Please enter a valid path or use the "Choose file" button!'
            self.showdialog(errortitle, errortext, additional = add_error)
        else:
            try:
                self.macrofile = self.filehandler.loadmacro(path)
                self.statustext = ''
                for i in range(len(self.macrofile['comments'])):
                    if self.macrofile['devices'][i] == 'DET':
                        self.statustext = self.statustext + self.macrofile['devices'][i] + '\t' + self.macrofile['commands'][i] + '\t' + self.macrofile['comments'][i] + '\n'
                    else:
                        self.statustext = self.statustext + self.macrofile['devices'][i] + '\t' + self.macrofile['commands'][i] + '\t\t\t\t' + self.macrofile['comments'][i] + '\n'
                        
                self.runStatusTextEdit.setText(self.statustext)
                print(self.timestamp(), ': Macrofile', path, 'loaded!')
                self.autoStartButton.setEnabled(True)
                self.autoOnestepButton.setEnabled(True)
                self.ColoringActive.activate(0)
                
            except FileNotFoundError:
                errortitle = 'File not found'
                errortext  = 'The filename you entered can not be found!'
                add_error  = 'Please enter a valid path or use the "Choose file" button!'
                self.showdialog(errortitle, errortext, additional = add_error)
        
    def showdialog(self, title, text, additional = None, details = None, severity = 'Critical'):
        msg = QtWidgets.QMessageBox()
        
        if severity == 'Information':
            msg.setIcon(QtWidgets.QMessageBox.Information)
        elif severity == 'Question':
            msg.setIcon(QtWidgets.QMessageBox.Question)
        elif severity == 'Warning':
            msg.setIcon(QtWidgets.QMessageBox.Warning)
        elif severity == 'Critical':
            msg.setIcon(QtWidgets.QMessageBox.Critical)
        
        msg.setWindowTitle(title)
        msg.setText(text)
        
        if additional != None:
            msg.setInformativeText(additional)
        if details != None:
            msg.setDetailedText(details)
        
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        #msg.buttonClicked.connect(msgbtn)
        msg.exec_()
        
    def timestamp(self):
        return datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    
    def close_application(self):
        title = 'Exit'
        text  = 'Are you sure you want to quit the PanEDM Interface Application?'

        choice = QtWidgets.QMessageBox.question(self, title, text, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if choice == QtWidgets.QMessageBox.Yes:
            print(self.timestamp(), ': Exiting the program!')
            sys.exit()
        else:
            pass
    
    #Reroute the standard outputs to the window.
    def rerouteTerminalOutput(self):
        sys.stdout = EmittingStream()
        sys.stdout.textWritten.connect(self.WriteTerminalOutput)
        sys.stderr = EmittingStream()
        sys.stderr.textWritten.connect(self.WriteTerminalErrors)
        #Color settings of the Log section
        palette = QtGui.QPalette()
        #backgroundColor = QtGui.QColor(0, 0, 0)
        #palette.setColor(QtGui.QPalette.Base, backgroundColor)
        textColor = QtGui.QColor(255, 0, 0)
        palette.setColor(QtGui.QPalette.Text, textColor)
        self.critical_text.setPalette(palette)

    def WriteTerminalOutput(self, text):
        #Append output to log file
        file = open(self.logFilePath + 'PanEDM_Interface_Log_' + datetime.datetime.now().strftime("%Y-%m-%d") + '.txt', 'a')
        file.write(text)
        file.close()
        
        #Write output to window log widget
        cursor = self.all_text.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.all_text.setTextCursor(cursor)
        self.all_text.ensureCursorVisible()
    
    def WriteTerminalErrors(self, text):
        cursor = self.critical_text.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.critical_text.setTextCursor(cursor)
        self.critical_text.ensureCursorVisible()
        #self.WriteTerminalOutputFull(text)

    def about(self):
        self.InfoWin = Infowindow()
        self.InfoWin.show()
        self.InfoWin.closeSignal.connect(self.closeInfo)
        
    def closeInfo(self):
        del(self.InfoWin)
    
    def UserLogin(self):
        self.LoginWindow = Login(self.firstLogin)
        self.LoginWindow.show()
        self.LoginWindow.Ok.connect(self.LoginOk)
        self.LoginWindow.Cancel.connect(self.LoginCancel)
    
    def LoginOk(self, data):
        self.user = data
        if self.user['Name'] == '' or self.user['eMail'] == '':
            title      = 'No User Information!' 
            text       = 'You have not entered complete user information!'
            additional = 'Since these information are included in the log files, you can not leave them empty!'
            self.showdialog(title, text, additional = additional)
            
        else:
            self.username.setText(self.user['Name'])
            print(self.timestamp() + ' : User logged in. The current user is ' + self.user['Name'])
            del(self.LoginWindow)
            self.firstLogin = False
        
    def LoginCancel(self):
        del(self.LoginWindow)
        
    def Settings(self):
        self.SettingsWindow = Settings()
        self.SettingsWindow.show()
    

#Function to run the application
def run_Application():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = PanEDM_Interface()
    MainWindow.show()
    sys.exit(app.exec_())

#Run the application if this file is directly loaded.
if __name__ == "__main__":
    run_Application()
