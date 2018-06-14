import datetime


#Class for handling of all the ASCII files (Macro files, command files and return files)
class read_write_files(object):
    def __init__(self, **kwargs):
        super(read_write_files, self).__init__()
        
        #Class variables:
        self.macro_vars = {'devices' : [], 'commands' : [], 'comments' : []}
        
    #Class method for the loading of the macro file.
    #It returns the columns of the macro file in separate lists. This method only works in combination with
    #the method check_include(self). The two methods are called by each other in a recursive loop until all 
    #commands in all macro files are loaded.
    def loadmacro_worker(self, macrofile):
        file    = open(macrofile, 'r')
        lines   = file.readlines()

        for x in lines:
            if x[0] == '#' or len(x.split()) == 0:
                pass
            
            else:
                device_str  = x.split(';')[0].strip()
                command_str = x.split(';')[1].strip()
                comment_str = (x.split(';')[2].strip()).replace('#','')
                
                self.check_include(device_str, command_str)
                
                if self.included == False:
                    self.macro_vars['devices'].append(device_str)
                    self.macro_vars['commands'].append(command_str)
                    self.macro_vars['comments'].append(comment_str)
        
        file.close()
    
    #This method checks each line in the macro file wheter it's supposed to nest another macro file.
    #If so, it starts a recursion of the loadmacro method on the second macro file to include its commands
    def check_include(self, column_0_str, column_1_str):
        if column_0_str[0:7] == 'include':
            
            nest_file        = column_1_str
            repetitions      = int(column_0_str[7:])
            rep_var          = 0
            
  
            while rep_var < repetitions:
                rep_var += 1
                self.loadmacro_worker(nest_file)
                self.included    = True
                
        else:
            self.included    = False
            pass

    def loadmacro(self, macrofile):
        self.loadmacro_worker(macrofile)
        output          = self.macro_vars
        self.macro_vars = {'devices' : [], 'commands' : [], 'comments' : []}
        return output
    
    def write_command_file(self, user, device, command, comment, start_time, run_number, file_path):
        if device == 'DET':
            file     = open(file_path, 'w')
            comlist  = command.split(':')
            comstring = ';'+comlist[0]+';'+comlist[1]+';'+comlist[2]+';'+comlist[3]+';'+comlist[4]+';user='+user['Name'] 
            string   = 'Detector\tStart\tRamsey_' + datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + '_run_' + run_number + comstring
            file.write(string)
            file.close()
            
        else:
            file = open(file_path, 'w')
            file.write('User;\t\t\t\t' + user['Name'] + '\n')
            file.write('e-Mail;\t\t\t\t' + user['eMail'] + '\n')
            file.write('Subsystem;\t\t\t' + device + '\n')
            file.write('Run;\t\t\t\t' + run_number + '\n')
            file.write('StartTC;\t\t\t' + start_time + '\n')
            file.write('\n')
            file.write('Command;\t\t\t' + command + '\n')
            file.write('Last Update;\t\t' + datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + '\n')
            file.close()
            #print(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + ' : ' + comment)
        


if __name__ == '__main__':
    #The macrofile to be loaded:
    #macrofile = './Macrofiles/Macro.txt'

    #Create a file handler instance and read the macro file
    filehandler = read_write_files()
    #macro       = filehandler.loadmacro(macrofile)


    
