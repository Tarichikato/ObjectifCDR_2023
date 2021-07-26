import mouvements as mouvements
import math
import time
import talkToLL as ll
import get_config as gc



def execute_script():
    script = gc.get_script()
    f = open(script, "r")
    script = f.readlines()
    f.close()
    for instruction in script:
        translate_and_send(instruction)

def translate_and_send(instruction):
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

