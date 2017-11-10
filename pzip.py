#!/usr/bin/env python

import os
import sys
from multiprocessing import Process, Value
from threading import Semaphore, Thread
import zipfile
import argparse


def pyzip(args,t=False):
        global count
        
        if t==True:
                try:
                        for files in args:
                                if os.path.isfile(files):
                                        with zipfile.ZipFile(files+'.zip', mode='w') as zf:
                                                zf.write(files)
                                                
                                                count.value += 1
                                                
                                else:
                                     raise IOError 
                except:
                        print('File doesn\'t exist')
                        sys.exit()
        else:
                for files in args:
                        if os.path.isfile(files):
                                
                                with zipfile.ZipFile(files+'.zip', mode='w') as zf:
                                        zf.write(files)
                                        
                                        count.value += 1
                                        
def pyunzip(args,t=False):
        sem.acquire()
        global count
        if t==True:
                try:
                        for files in args:
                                if os.path.isfile(files):
                                        with zipfile.ZipFile(files) as zf:
                                                zf.extractall()
                                                count.value += 1
                                else:
                                        raise IOError
                except:
                        print('File doesn\'t exist')
                        sys.exit()
        else:
                for files in args:
                        if os.path.isfile(files):
                                with zipfile.ZipFile(files+'.zip', mode='w') as zf:
                                        zf.write(files)
                                        count.value += 1
        sem.release()


if __name__ == '__main__':
        #argumentos a utilizar
        parser = argparse.ArgumentParser(prog='pzip', description='Zip or unzip files')
        parser.add_argument('-c', action='store_const', dest='pyzip', const=True)
        parser.add_argument('-d', action='store_const', dest='pyunzip', const=True)
        parser.add_argument('-p', metavar='n', nargs='?', action='append', dest='process', const=True)
        parser.add_argument('-t', action='store_const', dest='targ', const=True)
        parser.add_argument('{ficheiros}', nargs='*')    
        args = parser.parse_args()
        count = Value('i',0)
        sem = Semaphore()
        #lista dos processos
        processes = []

        #verificação de argumentos
        if args.pyzip == True and args.pyunzip == None:
                if args.process:
                        if args.targ:
                                listArgs=[elem for elem in sys.argv[5:]]
                                if len(listArgs) == 0:
                                        end = 'y'
                                        while end != 'n':
                                                i_files = input('What file do you want to unzip? ')
                                                listArgs.append(i_files)
                                                end = input('Do you have more files(y, n)? ') 
                        else:
                                listArgs=[elem for elem in sys.argv[4:]]
                                if len(listArgs) == 0:
                                        end = 'y'
                                        while end != 'n':
                                                i_files = input('What file do you want to unzip? ')
                                                listArgs.append(i_files)
                                                end = input('Do you have more files(y, n)? ') 
                        for i in range(int(sys.argv[3])):
                                if args.targ:
                                        newT = Process(target=pyzip(listArgs,t==True))
                                else:
                                        newT = Process(target=pyzip(listArgs))

                                newT.start()
                                processes.append(newT)

                        for p in processes:
                                p.join()

			
                else:
                        
                        if args.targ:
                                listArgs=[elem for elem in sys.argv[3:]]
                                if len(listArgs) == 0:
                                        end = 'y'
                                        while end != 'n':
                                                i_files = input('What file do you want to unzip? ')
                                                listArgs.append(i_files)
                                                end = input('Do you have more files(y, n)? ') 
                                pyzip(listArgs,t=True)
                        else:
                                listArgs=[elem for elem in sys.argv[2:]]
                                if len(listArgs) == 0:
                                        end = 'y'
                                        while end != 'n':
                                                i_files = input('What file do you want to zip? ')
                                                listArgs.append(i_files)
                                                end = input('Do you have more files(y, n)? ') 
                                        pyzip(listArgs)
                                else:
                                        pyzip(listArgs)
                print('Foram zippados',count.value,'ficheiros')

        if args.pyunzip == True and args.pyzip == None:
                if args.process:
			
                        if args.targ:
                                listArgs=[elem for elem in sys.argv[5:]]
                                if len(listArgs) == 0:
                                        end = 'y'
                                        while end != 'n':
                                                i_files = input('What file do you want to unzip? ')
                                                listArgs.append(i_files)
                                                end = input('Do you have more files(y, n)? ') 
                        else:
                                listArgs=[elem for elem in sys.argv[4:]]
                                if len(listArgs) == 0:
                                        end = 'y'
                                        while end != 'n':
                                                i_files = input('What file do you want to unzip? ')
                                                listArgs.append(i_files)
                                                end = input('Do you have more files(y, n)? ') 
                        for i in range(int(sys.argv[3])):
                                if args.targ:
                                        newT = Process(target=pyunzip(listArgs,t==True))
                                else:
                                        newT = Process(target=pyunzip(listArgs))
                                
                                newT.start()
                                processes.append(newT)

                        for p in processes:
                                p.join()
                else:
                        if args.targ:
                                listArgs=[elem for elem in sys.argv[2:]]
                                if len(listArgs) == 0:
                                        end = 'y'
                                        while end != 'n':
                                                i_files = input('What file do you want to unzip? ')
                                                listArgs.append(i_files)
                                                end = input('Do you have more files(y, n)? ') 
                                        pyunzip(listArgs,t=True)
                                else:
                                        pyunzip(listArgs,t=True)
                                
                        else:
                                listArgs=[elem for elem in sys.argv[2:]]
                                if len(listArgs) == 0:
                                        end = 'y'
                                        while end != 'n':
                                                i_files = input('What file do you want to unzip? ')
                                                listArgs.append(i_files)
                                                end = input('Do you have more files(y, n)? ') 
                                        pyunzip(listArgs)
                                else:
                                        pyunzip(listArgs)
                print('Foram unzippados',count.value,'ficheiros')
        if args.pyzip == True and args.pyunzip == True:
                parser.error("-c and -d can't be used with eachother.")
	
