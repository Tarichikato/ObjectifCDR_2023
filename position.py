import talkToLL as talk_to_ll
import lidar as l
import balise as b


def compute_position():
    odometrie = talk_to_ll.get_position_odometrie()
    lidar = l.get_position()
    balise = b.get_robots_center()
    p = {'x': 0, 'y': 0, 'angle': 0}
    return p


def get_position():
    p = compute_position()
    return p
