import signal, time, sys
counter = 0
counter2 = 0
def handler(sig, NULL):
    global counter
    counter += 1
    print (str(counter) + " segundos")
    if counter == 15:
        sys.exit()

def controlC(sig, NULL):
    global counter2
    counter2+=1
    if counter <= 10:
        print ("carregou em ctrl+c " + str(counter2) + " vezes!")



signal.signal(signal.SIGALRM, handler)
signal.setitimer(signal.ITIMER_REAL, 1, 1)

if counter <= 10:
    signal.signal(signal.SIGINT, controlC)
else:
    signal.signal(signal.SIGINT, signal.SIG_IGN)

t1 = time.time()
time.sleep(0.5)
t2 = time.time()
print ("tempo aprox do sleep: " + str(t2-t1))

while True:
    time.sleep(1)
