import sys

class FileReader:
    """Reads a file"""

    def __init__(self, file):
        self.file = file


    def read_file_requests(self):
        try:
            with open(self.file, 'r') as inFile:
                reader = inFile.readlines()[7:]
                rqs_list = [l.strip().split(',') for l in reader]

        except IndexError:
            print("Error - Please specify an input file.")
            sys.exit(2)

        return rqs_list

    def read_file_operators(self):
        try:
            with open(self.file, 'r') as inFile:
                reader = inFile.readlines()[7:]
                opt_list = [l.strip().split(',') for l in reader]

        except IndexError:
            print("Error - Please specify an input file.")
            sys.exit(2)

        return opt_list

    def read_file_time(self):
        try:
            with open(self.file, 'r') as inFile:
                reader = inFile.readlines()[:7]
                lines = [l.strip().split(',') for l in reader]

        except IndexError:
            print("Error - Please specify an input file.")
            sys.exit(2)

        return lines[3]



#a = FileReader("requests14h55.txt")
#print(a.read_file_requests())
