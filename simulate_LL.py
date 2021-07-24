import _thread
import time
import math

class SimulatedLL():
    def __init__(self):
        self.x = 1000
        self.y = 500
        self.orientation = 0
        f = open("data/HLtoLL_move.txt", "w")
        f.write("")
        f.close()
        f = open("data/LLtoHL_move.txt", "w")
        f.write("")
        f.close()
        _thread.start_new_thread(self.listen_HL_move, (3,))
        # _thread.start_new_thread(self.listen_HL_actions, (3,))
        # _thread.start_new_thread(self.listen_HL_infos, (3,))
        _thread.start_new_thread(self.tell_HL_codeuses, (0.1,))

    def listen_HL_move(self,delay):
        l = 0
        while True:
            f = open("data/HLtoLL_move.txt", "r")
            message = f.readlines()
            f.close()
            if(l != len(message)):
                l = len(message)
                self.move_process(message[-1])
                f = open("data/LLtoHL_move.txt", "a")
                print("le LL renvoie {}".format(message[-1]))
                f.write(message[-1])
                f.close


    def listen_HL_actions(self,delay):
        l = 0
        while True:
            f = open("data/HLtoLL_move.txt", "r")
            message = f.readlines()
            f.close()
            if(l != len(message)):
                time.sleep(delay)
                l = len(message)
                f = open("data/LLtoHL_move.txt", "a")
                print("le LL renvoie {}".format(message[-1]))
                f.write(message[-1])
                f.close

    def listen_HL_infos(self,delay):
        l = 0
        while True:
            f = open("data/HLtoLL_move.txt", "r")
            message = f.readlines()
            f.close()
            if(l != len(message)):
                time.sleep(delay)
                l = len(message)
                f = open("data/LLtoHL_move.txt", "a")
                print("le LL renvoie {}".format(message[-1]))
                f.write(message[-1])
                f.close

    def tell_HL_codeuses(self,delay):
        while True:
            f = open("data/HLtoLL_codeuses.txt", "w")
            f.write("x_{}_y_{}".format(self.x,self.y))
            f.close()
            time.sleep(delay)

    def move_process(self,message):
        m = message.split("_")
        if(m[0] == "av"):
            l = int(m[1])
            step = l / abs(l) * 5
            for _ in range(abs(l) // 5):
                self.x += math.cos(self.orientation)*int(step)
                self.y += math.sin(self.orientation) * int(step)
                time.sleep(0.01)
            # Todo bouger de l'eventuel reliquat

        if (m[0] == "tt"):
            self.orientation = float(m[1])

