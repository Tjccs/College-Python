from file_reader import FileReader
from assigning import Operator_task
from file_writer import FileWriter
from dateTime import dateTime
import sys

class Main(FileReader, FileWriter):


    def __init__(self, file_1, file_2):
        FileReader.__init__(self, file_1)
        FileReader.__init__(self, file_2)
        FileWriter.__init__(self, file_1)
        #self.header_rq = FileWriter.__init__(self, file_2)

        
    def exec_operators(self):
        return self.read_file_operators()

    def exec_requests(self):
        return self.read_file_requests()

    def exec_timetable(self):
        
        timeTable = Operator_task(self.exec_operators(), self.exec_requests(), self.exec_time())
        timeTable_2 = timeTable.group_language()
        update_time = dateTime.add_minutes(5)
        file_op_name = 'operators' + update_time.replace(':', 'h') + '.txt'
        
        with open(file_op_name, 'w'):
            
            header = self.read_header()
            print(header)
            self.write_operators(operators, header, file_op_name)
            file_rq_name = 'timetable' + update_time.replace(':', 'h') + '.txt'
            
            result = self.write_assignments(timeTable_2, header, file_rq_name)
            print(result)
    
    
    def exec_time(self):
        return self.read_file_time()


    
    
    

if __name__ == "__main__":

    #a = Main(sys.argv[1], sys.argv[2])
    a = Main("operators14h55.txt", "requests14h55.txt")
    a.exec_timetable()
