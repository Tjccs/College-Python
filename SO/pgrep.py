#!/usr/bin/env python
# -*- coding: utf-8 -*-


from multiprocessing import Process, Value, Lock, Manager, Pool
from threading import Semaphore, Thread
import argparse, time, datetime, signal, sys, os, struct


def pgrep(list_files, text_pattern):
	"""Return the number of lines where the text appears.

	Args:
		list_files(list): The files that are going to be used.
		text_pattern(str): The text pattern to look for.
	
	Returns:
		The an int which is the number of lines where the pattern appears.
	
	Raise:
		IOError: If any of the input files doesn't exist.
	"""

	pass


if __name__ == '__main__':
	# argumentos a utilizar
	parser = argparse.ArgumentParser(prog='pgrep', description='Search files for matching words')
	parser.add_argument('-p', metavar='n', nargs='?', action='append', dest='process', const=True)
	parser.add_argument('ficheiros', nargs='*')
	parser.add_argument('texto', nargs='*') #pode precisar de ser alterado
	args = parser.parse_args()
	count = Value('i', 0)
	start_time = time.time()
	#lista dos processos
	processes = []
	sem = Semaphore(1)
	#verificação de argumentos
	p = False
	list_files = []
	for i in args.ficheiros:
		list_files.append(i)
	if len(list_files) == 0:
		#pedir ao utilizador nome dos ficheiros através do stdin(terminal)
		pass
	if args.process == None:
		newT = Process(target=pgrep, args=(list_files))
		newT.start()
		processes.append(newT)
	if args.process != None:
		p = True
		for i in range(int(args.process[0])):
			newT = Process(target=pgrep, args=(list_files, p))
			newT.start()
			processes.append(newT)
