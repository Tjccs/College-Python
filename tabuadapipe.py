import sys
import os
from multiprocessing import Process, Value, Array, Pipe


argm = int(sys.argv[1])
pipe_pai, pipe_filho = Pipe() 


def func_tab(pipe_filho):
    ar2 = pipe_filho.recv()
    
    for i in range(11):
        sm = argm * i
        ar2.append(sm)
    
    pipe_filho.send(ar2)

ar2 = []



newT = Process(target=func_tab, args=(pipe_filho,))
newT.start()
pipe_pai.send(ar2)
ar2 = pipe_pai.recv()

for i in range(11):
    print argm,'*',i,'=',ar2[i]
newT.join()


