import mouvements as mouvements
import math
import numpy as np
import time
import talkToLL as ll
import get_config as gc
import graph as graph
from scipy.spatial import distance


def execute_script(table):
    script = gc.get_script()
    f = open(script, "r")
    script = f.readlines()
    f.close()
    for instruction in script:
        translate_and_send(instruction,table)

def translate_and_send(instruction,table):
    instruction = instruction.split('_')
    instruction[-1] = instruction[-1].replace('\n',"")
    if(instruction[0] == "init-position"):
        x,y,o = interprete_init_arg(instruction[1:])
        ll.initiate_codeuses(x,y,o)
    elif(instruction[0] == "av"):
        arg = interprete_av_arg(instruction[1])
        mouvements.av(arg)
    elif (instruction[0] == "wait"):
        time.sleep(float(instruction[1]))
    elif (instruction[0] == "tt"):
        arg = interprete_tt_arg(instruction[1])
        mouvements.turn_to(arg)
    elif (instruction[0] == "sleep"):
        time.sleep(float(instruction[1]))
    elif (instruction[0] == "goto"):
        #Les déplacements sont fait dans l'interpreteur
        interprete_goto_arg(instruction[1:],table)

    else:
        print("Instruction inconnue : {}".format(instruction))

def interprete_init_arg(args):
    return(int(float(args[1])),int(float(args[3])),int(float(args[5])))

def interprete_av_arg(arg):
    return(float(arg))

def interprete_tt_arg(arg):
    # TODO Evidement changer ca
    if (arg.find('-pi') != -1):
        if (arg == '-pi'):
            arg = math.pi
        else:
            arg = arg.split('/')
            arg = -math.pi / float(arg[1])
        return (float(arg))
    if(arg.find('pi') != -1):
            if(arg == 'pi'):
                arg = math.pi
            else:
                arg = arg.split('/')
                arg = math.pi/float(arg[1])
            return (float(arg))

    return(float(arg))

def interprete_goto_arg(args,table):
    start = "{},{}".format(int(float(table.codeuses[0])),int(float(table.codeuses[1])))
    goal = "{},{}".format(int(float(args[1])),int(float(args[3])))
    path = graph.find_shortest_path(start,goal,table.graph)
    last_node = None
    for node in path:
        print("je dois aller de {} à {}".format(last_node,node))
        last_node = node
        node = node.split(",")



        s = (int(table.codeuses[0]),int(table.codeuses[1]))
        g = (int(float(node[0])),int(float(node[1])))

        d = float(distance.euclidean(s, g))
        print("je vais de {} à {}".format(s,g))
        if (d != 0):

            if(g[0]-s[0]==0 and g[1]-s[1]<0):
                angle = -math.pi/2
            elif (g[0] - s[0] == 0 and g[1] - s[1] > 0):
                angle = math.pi / 2
            elif (g[1] - s[1] == 0 and g[0] - s[0] < 0):
                angle = math.pi
            elif (g[1] - s[1] == 0 and g[0] - s[0] > 0):
                angle = 0
            else:
                angle = np.arctan((g[1]-s[1])/(g[0]-s[0]))
                if(g[0]-s[0]<0):
                    angle +=math.pi
            mouvements.turn_to(angle)
        mouvements.av(d)





def homologation():
    ll.initiate_codeuses(300,510,0)
    mouvements.turn_to(-0.63)
    mouvements.av(186)
    mouvements.turn_to(-math.pi/2)
    mouvements.av(260)
    mouvements.turn_to(0)
    mouvements.av(350)
    mouvements.turn_to(0.88)
    mouvements.av(426)
    mouvements.turn_to(math.pi/2)
    mouvements.av(430)
    mouvements.turn_to(0.96)
    mouvements.av(488)
    mouvements.turn_to(0)
    mouvements.av(450)
    mouvements.turn_to(math.pi/2)
    mouvements.av(400)
    mouvements.av(-400)

    mouvements.turn_to(math.pi)
    mouvements.av(1800-762)
    mouvements.turn_to(math.pi / 2)
    mouvements.av(500)
    mouvements.turn_to(math.pi)
    mouvements.av(400)
    mouvements.av(-400)
    mouvements.turn_to(-math.pi / 2)
    mouvements.av(600)
    mouvements.turn_to(0)
    mouvements.av(1500-762)
    mouvements.turn_to(-math.pi/2)


    time.sleep(3)

