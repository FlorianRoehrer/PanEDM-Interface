#Standard modules
import sys
import time
import numpy as np

#GUI class created by QtDesigner
from GUI.InfowindowGUI import *

#Main Window class. It inherits from the GUI class and adds the functionality
class Infowindow(QtWidgets.QMainWindow, Ui_Infowindow):
    
    closeSignal = QtCore.pyqtSignal()
    
    def __init__(self, **kwargs):
        super(Infowindow, self).__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        self.closeButton.clicked.connect(self.close)
        
    def close(self):
        self.closeSignal.emit()

#Function to run the application
def run_Application():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Infowindow()
    MainWindow.show()
    sys.exit(app.exec_())

#Run the application if this file is directly loaded.
if __name__ == "__main__":
    run_Application()
