#!/usr/bin/env python

import os
import sys
from multiprocessing import Process, Value
import zipfile
import argparse

count = Value('i',0)
def pyzip(args,t=False):
	global count
        if t==True:
                try:
                        for files in args:
                                with zipfile.ZipFile(files+'.zip', mode='w') as zf:
                                        zf.write(files)
                                        count.value += 1
                except:
                        sys.exit()
                        print('File doesn\'t exist')
	else:
		for files in args:
                        with zipfile.ZipFile(files+'.zip', mode='w') as zf:
                                zf.write(files)
                                count.value += 1
def pyunzip(args,t=False):
	global count
        if t==True:
                try:
	                for files in args:
		                with zipfile.ZipFile(files) as zf:
			                zf.extractall()
			                count.value += 1
                except:
                        sys.exit()
                        print('File doesn\'t exist')
        else:
                for files in args:
                        with zipfile.ZipFile(files+'.zip', mode='w') as zf:
                                zf.write(files)
                                count.value += 1



if __name__ == '__main__':
	#argumentos a utilizar
	parser = argparse.ArgumentParser(prog='pzip', description='Zip or unzip files')
	parser.add_argument('-c', action='store_const', dest='pyzip', const=True)
	parser.add_argument('-d', action='store_const', dest='pyunzip', const=True)
	parser.add_argument('-p', metavar='n', nargs='?', action='append', dest='process', const=True)
	parser.add_argument('-t', action='store_const', dest='targ', const=True)
	parser.add_argument('{ficheiros}', nargs='+')    
	args = parser.parse_args()

	#lista dos processos
	processes = []

	#verificação de argumentos
	if args.pyzip == True and args.pyunzip == None:

		if args.process:
                        if args.targ:
                                listArgs=[elem for elem in sys.argv[5:]]
                                
                        else:
                                listArgs=[elem for elem in sys.argv[4:]]

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
                        listArgs = []
			if args.targ:
                                for i in sys.argv[3:]:
                                        listArgs.append(i)
                                # Falta Codigo
                                pyzip(listArgs,t=True)
                        else:
                                for i in range sys.argv[2:]:
                                        listArgs.append(i)
                                if len(listArgs == 0):
                                        i_files = raw_input('Que ficheiro quer zipar? ')
                                        listArgs.append(i_files)
                                        pyzip(listArgs)
                                else:
                                        pyzip(listArgs)
		print('Foram zippados',count.value,'ficheiros')

        if args.pyunzip == True and args.pyzip == None:
		if args.process:
			
                         if args.targ:
                                listArgs=[elem for elem in sys.argv[5:]]
                                
                        else:
                                listArgs=[elem for elem in sys.argv[4:]]
			        
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
			listArgs = []
                        if args.targ:
                                for i in sys.argv[3:]:
                                        listArgs.append(i)
                                #Falta Codigo
                                pyunzip(listArgs,t=True)
                        else:
                                for i in sys.argv[2:]:
                                        listArgs.append(i)
                                if len(listArgs == 0):
                                        i_files = raw_input('Que ficheiro quer unzipar? ')
                                        listArgs.append(i_files)
                                        pyunzip(listArgs)
                                else:
                                        pyzip(listArgs)
                print('Foram unzippados',count.value,'ficheiros')
	if args.pyzip == True and args.pyunzip == True:
		parser.error("-c and -d can't be used with eachother.")
	
