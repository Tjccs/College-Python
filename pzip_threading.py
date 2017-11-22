#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from multiprocessing import Process, Value
from threading import Semaphore, Thread, Lock
import zipfile
import argparse
import time

def pyzip(args, t=False):
        global count
        
        if t == True:
                try:
                        
                        while count.value < len(args):
                                files = args[count.value]
                                count.value += 1
                                if os.path.isfile(files):
                                        with zipfile.ZipFile(files+'.zip', mode='w') as zf:
                                                
                                                zf.write(files)                                     
                                else:
                                     raise IOError 
                except:
                        print 'File doesn\'t exist'
                        sys.exit()
        else:
                while count.value < len(args):
                        files = args[count.value]
                        count.value += 1
                        if os.path.isfile(files):
                                
                                with zipfile.ZipFile(files+'.zip', mode='w') as zf:
                                        zf.write(files)
                             
def pyunzip(args, t=False):
        global count
        if t == True:
                try:
                        while count.value < len(args):
                                files = args[count.value]
                                count.value += 1
                                if os.path.isfile(files):
                                        with zipfile.ZipFile(files) as zf:
                                                zf.extractall()
                                        
                                else:
                                        raise IOError
                except:
                        print 'File doesn\'t exist'
                        sys.exit()
        else:
                while count.value < len(args):
                        files = args[count.value]
                        count.value += 1
                        if os.path.isfile(files):
                                with zipfile.ZipFile(files) as zf:
                                        zf.extractall()
                                        


if __name__ == '__main__':
        # argumentos a utilizar
        parser = argparse.ArgumentParser(prog='pzip', description='Zip or unzip files')
        parser.add_argument('-c', action='store_const', dest='pyzip', const=True)
        parser.add_argument('-d', action='store_const', dest='pyunzip', const=True)
        parser.add_argument('-p', metavar='n', nargs='?', action='append', dest='process', const=True)
        parser.add_argument('-t', action='store_const', dest='targ', const=True)
        parser.add_argument('{ficheiros}', nargs='*')    
        args = parser.parse_args()
        count = Value('i',0)
        threadLock = Lock()
        start_time = time.time()
        # lista dos threads
        threads = []

        #verificação de argumentos
        if args.pyzip == True and args.pyunzip == None:
                if args.process:
                        if args.targ:
                                listArgs = [elem for elem in sys.argv[5:]]
                                if len(listArgs) == 0:
                                        end = 'y'
                                        while end != 'n':
                                                i_files = raw_input('What file do you want to unzip? ')
                                                listArgs.append(i_files)
                                                end = raw_input('Do you have more files(y, n)? ') 
                        else:
                                listArgs = [elem for elem in sys.argv[4:]]
                                if len(listArgs) == 0:
                                        end = 'y'
                                        while end != 'n':
                                                i_files = raw_input('What file do you want to unzip? ')
                                                listArgs.append(i_files)
                                                end = raw_input('Do you have more files(y, n)? ') 
                        for i in range(int(sys.argv[3])):
                                if args.targ:
                                        t = True
                                        newT = Thread(target=pyzip, args=(listArgs, t,))
                                        newT.start()
                                else:
                                        newT = Thread(target=pyzip, args=(listArgs,))
                                        newT.start()
                                
                                threads.append(newT)

                        for t in threads:
                                t.join()

			
                else:
                        if args.targ:
                                listArgs = [elem for elem in sys.argv[3:]]
                                if len(listArgs) == 0:
                                        end = 'y'
                                        while end != 'n':
                                                i_files = raw_input('What file do you want to unzip? ')
                                                listArgs.append(i_files)
                                                end = raw_input('Do you have more files(y, n)? ') 
                                t = True
                                pyzip(listArgs, t)
                        else:
                                listArgs = [elem for elem in sys.argv[2:]]
                                if len(listArgs) == 0:
                                        end = 'y'
                                        while end != 'n':
                                                i_files = raw_input('What file do you want to zip? ')
                                                listArgs.append(i_files)
                                                end = raw_input('Do you have more files(y, n)? ') 
                                        pyzip(listArgs)
                                else:
                                        pyzip(listArgs)
                print 'Foram zippados',count.value,'ficheiros'
                print 'Tempo de execução: ',time.time() - start_time,'segundos'
        if args.pyunzip == True and args.pyzip == None:
                if args.process:
	                if args.targ:
                                listArgs = [elem for elem in sys.argv[5:]]
                                if len(listArgs) == 0:
                                        end = 'y'
                                        while end != 'n':
                                                i_files = raw_input('What file do you want to unzip? ')
                                                listArgs.append(i_files)
                                                end = raw_input('Do you have more files(y, n)? ') 
                        else:
                                listArgs = [elem for elem in sys.argv[4:]]
                                if len(listArgs) == 0:
                                        end = 'y'
                                        while end != 'n':
                                                i_files = raw_input('What file do you want to unzip? ')
                                                listArgs.append(i_files)
                                                end = raw_input('Do you have more files(y, n)? ') 
                        for i in range(int(sys.argv[3])):
                                if args.targ:
                                        t = True
                                        newT = Thread(target=pyunzip, args=(listArgs, t,))
                                        newT.start()
                                else:
                                        newT = Thread(target=pyunzip, args=(listArgs,))
                                        newT.start()
                                
                                threads.append(newT)

                        for t in threads:
                                t.join()
                else:
                        if args.targ:
                                listArgs = [elem for elem in sys.argv[2:]]
                                if len(listArgs) == 0:
                                        end = 'y'
                                        while end != 'n':
                                                i_files = raw_input('What file do you want to unzip? ')
                                                listArgs.append(i_files)
                                                end = raw_input('Do you have more files(y, n)? ') 
                                        t = True
                                        pyunzip(listArgs, t)
                                else:
                                        t = True
                                        pyunzip(listArgs, t)
                                
                        else:
                                listArgs = [elem for elem in sys.argv[2:]]
                                if len(listArgs) == 0:
                                        end = 'y'
                                        while end != 'n':
                                                i_files = raw_input('What file do you want to unzip? ')
                                                listArgs.append(i_files)
                                                end = raw_input('Do you have more files(y, n)? ') 
                                        pyunzip(listArgs)
                                else:
                                        pyunzip(listArgs)
                print 'Foram unzippados',count.value,'ficheiros'
                print 'Tempo de execução: ',time.time() - start_time,'segundos'
        if args.pyzip == True and args.pyunzip == True:
                parser.error("-c and -d can't be used with eachother.")
	
