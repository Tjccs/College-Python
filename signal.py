import signal, time, sys
counter = 0
def controlC(sig,NULL):
    global counter
    counter += 1
    print ("carregou em ctrl+c " + str(counter) + " vezes!")
def controlQuit(sig,NULL):
    print ("ok, sai " + str(counter) + " ctrl+c depois!")
    sys.exit() #termina o programa
signal.signal(signal.SIGINT, controlC)
signal.signal(signal.SIGQUIT, controlQuit)
while True:
    time.sleep(1)
    print ("C")
    print ("O")
    print ("C")
    print ("O")
    print ("M")
    print ("O")
    print ("---------------------------")