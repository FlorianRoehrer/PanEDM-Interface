#Standard modules
import sys
import time

#GUI class created by QtDesigner
from GUI.LoginGUI import *

#Main Window class. It inherits from the GUI class and adds the functionality
class Login(QtWidgets.QMainWindow, Ui_Login):
    
    Ok     = QtCore.pyqtSignal(dict)
    Cancel = QtCore.pyqtSignal()
    
    def __init__(self, first, **kwargs):
        super(Login, self).__init__()
        self.first = first
        self.setupUi(self)
        self.main()

    def main(self):
        if self.first == True:
            self.CancelButton.hide()
            
        self.OkButton.clicked.connect(self.OkFunc)
        self.CancelButton.clicked.connect(self.CancelFunc)
        
    def OkFunc(self):
        name = self.nameLineEdit.displayText()
        email = self.eMailLineEdit.displayText()
        data = {'Name' : name, 'eMail' : email}
        self.Ok.emit(data)
        
    def CancelFunc(self):
        self.Cancel.emit()
        
    def closeEvent(self, event):
        event.ignore()

#Function to run the application
def run_Application():
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = Login()
    LoginWindow.show()
    sys.exit(app.exec_())

#Run the application if this file is directly loaded.
if __name__ == "__main__":
    run_Application()
