import get_config as gc
import scripts as scripts

class Match():
    def __init__(self,table,robot):
        self.table = table
        self.robot = robot


    def execute_script(self):
        if(gc.is_homologation()):
            print("Debut du match en homologation")
            scripts.homologation()
            print("fin de l homologation")
