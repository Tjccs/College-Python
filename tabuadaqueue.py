import sys
import os
import time
from multiprocessing import Process, Value, Array, Pipe, Queue


argm = int(sys.argv[1])
q = Queue()

def func_tab(q):
    ar2 = q.get()
    
    for i in range(11):
        sm = argm * i
        ar2.append(sm)
    
    q.put(ar2)

ar2 = []



newT = Process(target=func_tab, args=(q,))
newT.start()

q.put(ar2)
time.sleep(1)
ar2 = q.get()

for i in range(11):
    print argm,'*',i,'=',ar2[i]
newT.join()
