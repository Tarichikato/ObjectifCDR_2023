import mouvements as mouvements
import math
import numpy as np
import time
import talkToLL as ll
import get_config as gc
import graph2 as graph

import copy
from scipy.spatial import distance


def execute_script(table):
    script = gc.get_script()
    f = open(script, "r")
    script = f.readlines()
    f.close()
    for instruction in script:
        print("instruction = {}".format(instruction))
        translate_and_send(instruction,table)

def translate_and_send(instruction,table):
    instruction = instruction.split('_')
    instruction[-1] = instruction[-1].replace('\n',"")
    if(instruction[0] == "init-position"):
        x,y,o = interprete_init_arg(instruction[1:])
        ll.initiate_codeuses(x,y,o)
        while(table.codeuses != (x,y,o)):
            table.update_table()
        print("Codeuses initialisées pour la table. Table truth : {}. Init : {}".format(table.codeuses,(x,y,o)))
    elif(instruction[0] == "av"):
        arg = interprete_av_arg(instruction[1])
        mouvements.av(arg)
    elif (instruction[0] == "wait"):
        time.sleep(int(instruction[1]))
    elif (instruction[0] == "tt"):
        arg = interprete_tt_arg(instruction[1])
        mouvements.turn_to(arg)
    elif (instruction[0] == "sleep"):
        time.sleep(int(instruction[1]))
    elif (instruction[0] == "goto"):
        #Les déplacements sont fait dans l'interpreteur
        interprete_goto_arg(instruction[1:],table)

    else:
        print("Instruction inconnue : {}".format(instruction))

def interprete_init_arg(args):
    return(int(args[1]),int(args[3]),int(args[5]))

def interprete_av_arg(arg):
    return(int(arg))

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
    #TODO Regler le problème de si on est pas sur un noeud du graph
    if(table.codeuses[0] % 250 != 0 or table.codeuses[1] % 250 != 0):
        x = round(table.codeuses[0]/250)*250
        y = round(table.codeuses[1] / 250) * 250
        start = (int(x), int(y))
    else:
        start = (int(table.codeuses[0]),int(table.codeuses[1]))
    goal = (int(args[1]),int(args[3]))

    path = graph.find_shortest_path(start,goal,table.graph,table.nodes)
    last_node = None
    last_angle = None
    instructions = []
    if(path != None):
        path = path[1:]
        print(path)
        last_node = None
        for node in path:
            #print("je dois aller de {} à {}".format(last_node,node))



            if (last_node == None):
                s = (int(table.codeuses[0]),int(table.codeuses[1]))
            else:
                s = (int(last_node[0]), int(last_node[1]))
            g = (int(node[0]),int(node[1]))
            last_node = node


            d = int(distance.euclidean(s, g))
            #print("je vais de {} à {}".format(s,g))
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
                if (last_angle != angle):
                    instructions.append("tt_{}".format(angle))
                    last_angle = angle
            instructions.append("av_{}".format(d))
        execute__mouvement_instruction_list(instructions)

    else:
        print("Je trouve pas de chemin")
        print("je dois aller de {} à {}".format(start, goal))
        time.sleep(2)

        interprete_goto_arg(args, table)

def execute__mouvement_instruction_list(list):
    i = 0
    while(i<len(list)):
        inst = list[i]
        if(inst[0] == 't'):
            order = inst.split('_')
            mouvements.turn_to(float(order[1]))
            i+=1
        elif(inst[0] == 'a'):
            d = 0
            while(i<len(list) and list[i][0] == 'a' ):
                inst = list[i]
                order = inst.split('_')
                d+=int(order[1])
                i+=1
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

