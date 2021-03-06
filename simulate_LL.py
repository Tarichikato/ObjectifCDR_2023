import _thread
import time
import math

class SimulatedLL():

    def __init__(self):
        self.right_to_move = False
        self.x = 0
        self.y = 0
        self.vitesse = 500 #On traverse la table en 6 secondes
        self.orientation = 0
        f = open("data/HLtoLL_move.txt", "w")
        f.write("")
        f.close()
        f = open("data/LLtoHL_move.txt", "w")
        f.write("")
        f.close()
        f = open("data/HLtoLL_info.txt", "w")
        f.write("")
        f.close()
        f = open("data/LLtoHL_info.txt", "w")
        f.write("")
        f.close()
        _thread.start_new_thread(self.listen_HL_right_to_move, (0.01,))
        _thread.start_new_thread(self.listen_HL_infos, (3,))
        _thread.start_new_thread(self.listen_HL_move, (3,))
        # _thread.start_new_thread(self.listen_HL_actions, (3,))
        _thread.start_new_thread(self.tell_HL_codeuses, (0,))

    def listen_HL_right_to_move(self,delay):
        while True:
            f = open("data/HLtoLL_right_to_move.txt", "r")
            right = f.read()
            f.close()
            self.right_to_move = bool(right)
            time.sleep(delay)



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
                #print("le LL renvoie {}".format(message[-1]))
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
                #print("le LL renvoie {}".format(message[-1]))
                f.write(message[-1])
                f.close

    def listen_HL_infos(self,delay):
        l = 0
        while True:
            f = open("data/HLtoLL_info.txt", "r")
            message = f.readlines()
            f.close()
            if(l != len(message)):
                l = len(message)
                last_message = message[-1]

                if(last_message.split('_')[0] == "init-codeuses"):
                    self.init_codeuses(last_message)
                _last_message = last_message.split('_')
                f = open("data/LLtoHL_info.txt", "a")
                #print("le LL renvoie {}".format(last_message))
                f.write(last_message)
                f.close

    def tell_HL_codeuses(self,delay):
        while True:
            f = open("data/LLtoHL_codeuses.txt", "w")
            f.write("x_{}_y_{}_o_{}".format(self.x,self.y,self.orientation))
            f.close()
            time.sleep(delay)

    def move_process(self,message):
        m = message.split("_")
        if (m[0] == "av" and int(m[1]) != 0):
            x= math.cos(self.orientation) * int(m[1])
            y= math.sin(self.orientation) * int(m[1])
            _x,_y = self.x,self.y
            for _ in range (10):
                while not self.right_to_move:
                    print("Je ne peux pas bouger")
                    time.sleep(1)
                self.x += int(x/10)
                self.y += int(y/10)
                time.sleep(int(m[1])/self.vitesse/10)
            #C'est bien joli d'avancer doucement mais bon..
            self.x = _x + int(x)
            self.y = _y + int(y)
        if (m[0] == "tt"):
            self.orientation = float(m[1])


    def init_codeuses(self,last_message):
        last_message = last_message.split('_')
        self.x = int(last_message[2])
        self.y = int(last_message[4])
        self.orientation = float(last_message[6])

