import time
import copy
from multiprocessing import Array

t = time.time()
lista = [elem for elem in range(1,501)]

k = copy.copy(lista)

l = Array("i",k)

for i in range(500):
    print (l[i])
print ("demorou",time.time() - t)

