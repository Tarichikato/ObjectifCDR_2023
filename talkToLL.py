import get_config as gc
import time

#GET DATA

def get_position_odometrie():
    #print('je demande ma position au LL selon les codeuses')
    #Todo Com LL
    position = None
    return(position)

#MOVE ORDERS

def av(l):
    if(gc.is_ll_simulated()):
        f = open("data/HLtoLL.txt", "a")
        print("Le HL envoie {}".format("av_{}\n".format(l)))
        f.write("av_{}\n".format(l))
        f.close
        for k in range (100):
            f = open("data/LLtoHL.txt", "r")
            message = f.readlines()
            if("av_{}\n".format(l) in message):
                f.close()
                print("le HL a bien recu {}".format("av_{}\n".format(l)))
                return(0)
            f.close()
            time.sleep(0.5)