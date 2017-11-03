from multiprocessing import Process, Array, Semaphore
import random, time

MAX_SIZE = 5
buffer = Array("i",MAX_SIZE)

empty = Semaphore(MAX_SIZE) #Inicialmente, MAX_SIZE posicoes livres
full = Semaphore(0) #Inicialmente, 0 posicoes ocupadas

def produtor():
 	inPosition = 0
	while True:
		nextProduced = random.randint(1,100)
		empty.acquire() #Ha’ posicoes livres?
		buffer[inPosition] = nextProduced
		temp = inPosition
		inPosition = (inPosition + 1) % MAX_SIZE
		full.release() #Informo que há nova posicao ocupada
		print "+++Produzi " + str(nextProduced) + " na posicao " + str(temp)
		time.sleep(random.randint(0,3)) #descanso um pouco

def consumidor():
	 outPosition = 0
	 while True:
		full.acquire()
	 	tmp = outPosition
		nextConsumed = buffer[outPostion]
		
		outPosition = (outPosition + 1) % MAX_SIZE
		
		empty.release()
		time.sleep(random.randint(0,3)) #descanso um pouco
prod = Process(target=produtor)
cons = Process(target=consumidor)
prod.start()
cons.start()
prod.join()
cons.join()
