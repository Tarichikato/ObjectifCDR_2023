import talkToLL as ll
import math

def av(l):
    ll.av(l)

def turn_to(o):
    PI = math.pi
    while (o > PI) : o -= 2 * PI
    while (o < -PI) :o += 2 * PI
    ll.tt(o)
