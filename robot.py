import _thread
import time
import get_config as gc
import position as position
from scipy.spatial import distance
import  talkToLL as ll

class Robot():

    def __init__(self,table):
        self.table = table
        self.right_to_move = False
        self.name = gc.get_name()
        self.robot_ray = 200


        self.position = self.get_position()

        _thread.start_new_thread(self.keep_position_updated, (0.1,))
        _thread.start_new_thread(self.update_right_to_move, (0.01,))

    def keep_position_updated(self,delay):
        while True:
            self.position = self.get_position()
            time.sleep(delay)

    def get_position(self):
        p= self.table.codeuses
        return(p)

    def update_right_to_move(self,delay):
        while True:
            enemy = self.table.bd['enemy_1'] # TODO a remplacer par moving obstacles
            d = int(distance.euclidean(enemy, self.position[:2]))
            if(d < self.robot_ray * 2):
                self.right_to_move = False
                ll.update_right_to_move(self.right_to_move)
            elif not self.right_to_move:
                self.right_to_move = True
                ll.update_right_to_move(self.right_to_move)

            time.sleep(delay)
