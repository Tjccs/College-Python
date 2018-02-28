import sys

class FileReader:
    """Reads a file"""
    def __init__(self, files):
        input = ''
        try:
            with open(files, 'r') as inFile:
                lines = [l for l in inFile]
                
        except IndexError:
            print("Error - Please specify an input file.")
            sys.exit(2)