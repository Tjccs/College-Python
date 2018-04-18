#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 13:10:59 2018

@author: fc48286
"""

import file_reader
import file_writer
import dateTime
import operator
import itertools

class Operator_task:

    def __init__(self, operators, requests, current_time):
        self.operators = operators
        self.request = requests
        self.current_time = current_time

    def sorting(self):
        operators_list = self.operators
        operators_sorted = sorted(operators_list, key=operator.itemgetter(3,4,0))
        return operators_sorted

    def group_language(self):
        attendance_list = []
        op = self.sorting()
        rq = self.request

        for x in range(len(rq)):
            for y in range(len(op)):
                if (op[y][1] == rq[x][1]) and (rq[x][2] in op[y][2]) and (op[y][4] == rq[x][4]) and (int(rq[x][4]) <= 240):
                    time_operator = max(self.current_time[0],op[y][3])
                    time_operator_split = time_operator.split(':')
                 
                    k = dateTime.dateTime(int(time_operator_split[0]), int(time_operator_split[1]))
                    
                    op[y][3] = k.add_minutes(int(rq[x][4]))
                    op[y][4] += rq[x][4]
                    #attendance_list.append([time_operator, rq[x][0], op[y][0]])


                else:
                    op[y][4] = op[y][4] + rq[x][4]

                    time = op[y][3].split(':')
                    time_rq = rq[x][4]

                    inc = dateTime.dateTime(time[0], time[1])
                    inc_rq = dateTime.dateTime(time[0], time[1])

                    op[y][3] = inc.add_minutes(int(rq[x][4]))
                    attendance_list.append([self.current_time, rq[x][0], 'not-assigned'])


        attendance_sorted = sorted(attendance_list, key=operator.itemgetter(0,1))
        result = [k for k,_ in itertools.groupby(attendance_sorted)]
        return result

#a = Operator_task([['Ricardo Tavares', ' portuguese', ' (mobiles; printers)', ' 15:15', ' 42'], ['Carl Thompson', ' english', ' (laptops)', ' 14:17', ' 54'], ['Nuria Castro', ' spanish', ' (cameras; hifi)', ' 14:24', ' 37'], ['Giovanni Olivetti', ' italian', ' (laptops; bimby; hifi)', ' 14:52', ' 21'], ['Georg Muller', ' deutsch', ' (cameras)', ' 15:05', ' 31']], [['Henry Miller', ' english', ' laptops', ' premium', ' 3'], ['Francois Greenwich', ' spanish', ' cameras', ' premium', ' 6'], ['Ricardo Carvalho', ' portuguese', ' refrigerators', ' premium', ' 2']], '14:55')
#print(a.group_language())
