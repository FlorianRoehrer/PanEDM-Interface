#Standard modules
import sys
import time

#GUI class created by QtDesigner
from GUI.SettingsGUI import *

#Settings Window class. It inherits from the GUI class and adds the functionality
class Settings(QtWidgets.QMainWindow, Ui_Settings):
    
    Ok     = QtCore.pyqtSignal()
    Cancel = QtCore.pyqtSignal()
    
    def __init__(self, **kwargs):
        super(Settings, self).__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        pass

#Function to run the application
def run_Application():
    app = QtWidgets.QApplication(sys.argv)
    SettingsWindow = Settings()
    SettingsWindow.show()
    sys.exit(app.exec_())

#Run the application if this file is directly loaded.
if __name__ == "__main__":
    run_Application()
