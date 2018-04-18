#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 13:20:52 2018

@author: fc48286
"""

import dateTime
import file_reader

class FileWriter:

    def __init__(self, file):
        self.file = file

    def group(self, lst):
        for i in range(0, len(lst), 2):
            val = lst[i:i+2]
            if len(val) == 2:
                yield tuple(val)

    def read_header(self):

        present_time = file_reader.FileReader(self.file)
        present_time2 = present_time.read_file_time()[0]

        time_split = present_time2.split(':')

        inc_time = dateTime.dateTime(time_split[0], time_split[1])
        inc_time = inc_time.add_minutes(present_time2, 5)


        try:
            with open(self.file, 'r') as inFile:
                reader = inFile.readlines()[:6]
                lines = list(self.group(reader))
                final_list = 'Day: \n'+lines[0][1]+'Time: \n'+inc_time+'\n'+'Company: \n'+'NSHF'


        except IndexError:
            print("Error - Please specify an input file.")
            sys.exit(2)


        return final_list

    def write_operators(self,operators,final_list,operators_file):

        try:
            with open(operators_file, "w+") as op_file:
                op_file.write(str(final_list)+'\nOperators:\n')

                for i in range(len(operators)):
                    for j in range(len(operators)-1):
                        op_file.write(str(operators[i][j]+', '))

                    op_file.write(str(operators[i][4]))
                    op_file.write("\n")


        except IndexError:
            print("Error - Please specify an input file.")
            sys.exit(2)

        return op_file

    def write_assignments(self,timeTable, final_list,requests_file):

        try:
            with open("k.txt", "w+") as rq_file:
                rq_file.write(str(final_list)+'\nTimeTable:\n')

                for a in range(len(timeTable)):
                    for b in range(len(timeTable[a])-1):
                        rq_file.write(str(timeTable[a][b]+', '))

                    rq_file.write(str(timeTable[a][2]))
                    rq_file.write("\n")

        except IndexError:
            print("Error - Please specify an input file.")
            sys.exit(2)

        return rq_file
