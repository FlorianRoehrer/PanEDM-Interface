import time
from PyQt5 import QtCore
from Modules.read_write_files import *

class comm_write_worker(QtCore.QObject):
    
    file_written   = QtCore.pyqtSignal()
    macro_finished = QtCore.pyqtSignal()
    wait_signal    = QtCore.pyqtSignal(str)
    
    def __init__(self, user, macrocontent, start_time, run_number, dev_file):
        super(comm_write_worker, self).__init__()
        self.writer       = read_write_files()
        self.dev_paths    = {'devices' : [], 'paths' : []}
        self.macro        = macrocontent
        self.start_time   = start_time
        self.run_number   = run_number
        self.dev_file     = dev_file
        self.user         = user
        
    def startRun(self):
        self.runInstance = self.runGenerator()
        
    def runGenerator(self):
        self.get_device_paths(self.dev_file)
        index = 0
        for i in range(len(self.macro['devices'])):
            if self.macro['devices'][i] == 'WAIT':
                print(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + ' : ' + 'Waiting for ' + self.macro['commands'][i] + ' seconds!')
                self.wait_signal.emit(self.macro['commands'][i])
                
            else:
                print(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + ' : ' + self.macro['devices'][i] + '; ' + self.macro['commands'][i] + '; #' + self.macro['comments'][i])
                self.writer.write_command_file(self.user, self.macro['devices'][i], self.macro['commands'][i], self.macro['comments'][i], self.start_time, self.run_number, self.dev_paths['paths'][self.dev_paths['devices'].index(self.macro['devices'][i])])
                
            self.file_written.emit()
            if index == len(self.macro['devices']):
                self.macro_finished.emit()
            index += 1
            yield
            
    def get_device_paths(self, dev_file):
        file    = open(dev_file, 'r')
        lines   = file.readlines()

        for x in lines:
            if x[0] == '#' or len(x.split()) == 0:
                pass
            
            else:
                device_str  = x.split(';')[0].strip()
                path_str    = x.split(';')[1].strip()
                self.dev_paths['devices'].append(device_str)
                self.dev_paths['paths'].append(path_str)
        
        file.close()
        
        
        
        
