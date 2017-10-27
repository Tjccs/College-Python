import sys
import os
from multiprocessing import Process, Value

lista = []
lista.append(int(sys.argv[1]))
lista.append(int(sys.argv[2]))
lista.append(int(sys.argv[3]))
lista.append(int(sys.argv[4]))
lista.append(int(sys.argv[5]))

soma = Value("i", 0)

def func_soma():
    global soma
    soma.value = sum(lista)
    print os.getpid()
    
newT = Process(target=func_soma)
newT.start()
newT.join()

print os.getpid()
print soma.value



