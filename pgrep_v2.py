#!/usr/bin/env python
# -*- coding: utf-8 -*-


from multiprocessing import Process, Value, Queue, Semaphore
import argparse
import re
import os
import sys

q = Queue() #inicialização da queue
sem = Semaphore(1) #inicialização do semáforo
n = Value('i',0) #inicialização da variável partilhada

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
	num_linhas = 0
	for file in list_files:
		if not os.path.isfile(file):
			print ('O Ficheiro %s não existe') % file
			sys.exit(0)
		else:
			q.put(file)
			with open(file, 'r') as f:
				for text in text_pattern:  # para cada string na lista do conjunto de argumentos,
					output = f.readlines()  # conteúdo do ficheiros em listas (cada linha representada por uma string)
					for linha in output:  # linha - string
						palavras = list(set(linha.split('\n'))) # faz lista de todas as palavras (strings) da linha
						for palavra in palavras:
								procura = re.search(text, palavra)  # procura a string text (dada na linha de comandos) na string palavra
								if procura is not None:
									num_linhas += 1  # contabiliza o numero de linhas em que a palavra/letra aparece
									n.value += 1

	return n

print('O numero de linhas = ', n)

if __name__ == '__main__':
	# argumentos a utilizar
	parser = argparse.ArgumentParser(prog='pgrep', description='Search files for matching words')
	parser.add_argument('-p', metavar='n', nargs='?', action='append', dest='process', const=True)
	parser.add_argument('ficheiros', nargs='*')
	parser.add_argument('-t', nargs='*', dest="text")
	args = parser.parse_args()
	# verificação de argumentos
	p = False
	process_list = list()
	list_files = [i for i in args.ficheiros]

	while len(list_files) == 0:
		files = input("Indique o/(s) nome/(s) do/(s) ficheiro/(s): ")
		list_files = files.split(' ')

	if args.process is None:  # if number of processes not given
		newP = Process(target=pgrep, args=(list_files, args.text))
		newP.start()
	else:
		p = True
		for i in range(int(args.process[0])):
			newP = Process(target=pgrep, args=(list_files, args.text))
			process_list.append(newP)
			newP.start()
		for p in process_list:
			p.join()
