from PyQt5 import QtCore
#___________________________________________________________________________________________


#This class reroutes the Python standard output to the GUI window
class EmittingStream(QtCore.QObject):

    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))
        
    def flush(self):
        pass
