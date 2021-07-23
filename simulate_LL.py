import _thread
import time

def init_simulated_LL():
    _thread.start_new_thread(listen_HL, (3,))

def listen_HL(delay):
    l = 0
    while True:
        f = open("data/HLtoLL.txt", "r")
        message = f.readlines()
        f.close()
        if(l != len(message)):
            l = len(message)
            f = open("data/LLtoHL.txt", "a")
            print("le LL renvoie {}".format(message[-1]))
            f.write(message[-1])
            f.close

        time.sleep(delay)

