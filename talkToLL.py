import get_config as gc
import time

#GET DATA

def get_position_odometrie():
    f = open("data/LLtoHL_codeuses.txt", "r")
    codeuses = f.read()
    f.close()
    data = codeuses.split("_")
    return(data)

#MOVE ORDERS

def initiate_codeuses(x,y,o):
    f = open("data/LLtoHL_info.txt", "r")
    id = len(f.readlines())
    f.close
    f = open("data/HLtoLL_info.txt", "a")
    f.write('init-codeuses_x_{}_y_{}_o_{}\n'.format(x,y,o))
    f.close
    #print("Le HL envoie {}".format('init-codeuses_x_{}_y_{}_o_{}\n'.format(x,y,o)))
    for k in range(20):
        f = open("data/LLtoHL_info.txt", "r")
        message = f.readlines()
        if ('init-codeuses_x_{}_y_{}_o_{}\n'.format(x,y,o) in message[id:]):
            f.close()
            #print("le HL a bien recu {}".format('init-codeuses_x_{}_y_{}_o_{}'.format(x,y,o)))
            return (0)
        f.close()
        #time.sleep(0.5)



def av(l):
    send('av',l)

def tt(o):
    send('tt',o)

def update_right_to_move(right):
    f = open("data/HLtoLL_right_to_move.txt", "w")
    if(right):
        f.write("{}".format(right))
    else:
        f.write("")
    f.close()

def send(order,a):
    if (gc.is_ll_simulated()):
        f = open("data/LLtoHL_move.txt", "r")
        id = len(f.readlines())
        f.close
        f = open("data/HLtoLL_move.txt", "a")
        #print("Le HL envoie {}".format("{}_{}\n".format(order,a)))
        f.write("{}_{}\n".format(order,a))
        f.close
        #TODO gerer les cas ou le LL répond pas
        for k in range(20):
            f = open("data/LLtoHL_move.txt", "r")
            message = f.readlines()
            if ("{}_{}\n".format(order,a) in message[id:]):
                f.close()
                #print("le HL a bien recu {}".format("{}_{}\n".format(order,a)))
                return (0)
            f.close()
            time.sleep(0.5) #Comme ca on attend au pire 10s

