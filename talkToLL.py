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
        time.sleep(2)
        print("J'ai avancé de {} mm".format(l))