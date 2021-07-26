import get_config as gc
import scripts as scripts

class Match():
    def __init__(self,table,robot):
        self.table = table
        self.robot = robot


    def execute_script(self):
        scripts.execute_script()
