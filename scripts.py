import mouvements as mouvements
import math
import time
import talkToLL as ll

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

