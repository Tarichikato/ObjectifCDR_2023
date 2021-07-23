import _thread
import time
import get_config as gc
import position as position

class Robot():

    def __init__(self):

        self.name = gc.get_name()


        self.position = self.get_position()

        _thread.start_new_thread(self.keep_position_updated, (0.1,))

    def keep_position_updated(self,delay):
        while True:
            self.position = self.get_position()
            time.sleep(delay)

    def get_position(self):
        p= position.get_position()
        return(p)