from PyQt5 import QtCore
import time
#___________________________________________________________________________________________


#Class to execute the function which is handed over in the __init__() method infinitely in 
#defined timesteps. to start a timer, first create an instance of the class. The loop can be
#started by calling <instance name>.start_loop(<interval>). Stop the loop by invoking 
#<instance name>.stop_loop()
class function_timer(QtCore.QObject, object):
    
    executeSignal = QtCore.pyqtSignal()
    
    def __init__(self, function = None, **kwargs):
        super(function_timer, self).__init__()
        self.function  = function
        self.waiting   = False
        self.generator = None
        self.timer     = None
    
    def create_loop(self, function):
        #self.count = 0
        while True:
            function()
            yield
            
    def ClockEvent(self):
        if self.waiting == True:
            self.waiting = False
            self.timer.setInterval(self.interval)
        
        elif self.waiting == False:
            if self.activeInterval != self.interval:
                self.timer.setInterval(self.interval)
        try:
            if self.function == None:
                self.executeSignal.emit()
            else:
                next(self.generator)
                self.executeSignal.emit()
                
        except StopIteration:
            self.stop_loop()
    
    def stop_loop(self):
        try:
            if self.timer != None:
                self.timer.stop()
        except:
            pass
        self.generator = None
        self.timer = None
    
    def change_interval(self, msecs):
        self.timer.setInterval(msecs)
        
    def wait(self, msecs):
        if self.timer == None:
            pass
        else:
            self.waiting = True
            self.activeInterval = msecs
            self.timer.setInterval(msecs)
        
    def start_loop(self, interval):
        self.interval = interval
        self.activeInterval = interval
        self.stop_loop()
        if self.generator == None and self.function != None:
            self.generator = self.create_loop(self.function)
        self.timer = QtCore.QTimer()
        self.timer.start(self.interval)
        self.timer.timeout.connect(self.ClockEvent)

