#!/usr/bin/env python

import os
import sys
from multiprocessing import Process
import zipfile
import argparse

def pyzip(args):
    
    
    print(args)
  

def pyunzip(args2):
    
    print(args2)

    
if __name__ == '__main__':
    #argumentos a utilizar
    parser = argparse.ArgumentParser(prog='pzip', description='Zip or unzip files')
    parser.add_argument('-c', action='store_const', dest='pyzip', const=True)
    parser.add_argument('-d', action='store_const', dest='pyunzip', const=True)
    parser.add_argument('-p', metavar='n', nargs='?', action='append', dest='process', const=True)
    args = parser.parse_args()
    
    #lista dos processos
    processes = []
    
    #verificação de argumentos
    if args.pyzip == True and args.pyunzip == None:
        if args.process:
            for i in range(int(sys.argv[3])):
                newT = Process(target=pyzip('files'))
                newT.start()
                processes.append(newT)
            for p in processes:
                p.join()
            print(args.pyunzip)
            print(args.pyzip)
        else:
            pyzip('No Process')
    
    if args.pyunzip == True and args.pyzip == None:
        if args.process:
            for i in range(int(sys.argv[3])):
                newT = Process(target=pyunzip('files'))
                newT.start()
                processes.append(newT)
            for p in processes:
                p.join()           
        else:
            pyunzip('No Process')
    else:
        parser.error("-c and -d can't be used with eachother.")
