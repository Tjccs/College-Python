import sys

class FileReader:
    """Reads a file"""

    def __init__(self, file):
        self.file = file


    def read_file(self):
        try:
            with open(self.file, 'r') as inFile:
                reader = inFile.readlines()[7:]
                lines = [l.strip().split(',') for l in reader]

        except IndexError:
            print("Error - Please specify an input file.")
            sys.exit(2)

        return lines

    def read_file_time(self):
        try:
            with open(self.file, 'r') as inFile:
                reader = inFile.readlines()[:7]
                lines = [l.strip().split(',') for l in reader]

        except IndexError:
            print("Error - Please specify an input file.")
            sys.exit(2)

        return lines[3]

