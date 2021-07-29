
from table import Table
from robot import Robot
from match import Match
import _thread
from simulate_LL import SimulatedLL
import display
import time
import graph2 as g2

if __name__ == '__main__':



    ll = SimulatedLL()
    table = Table()
    print("End of init table")
    robot = Robot(table)





    match = Match(table, robot)

    _thread.start_new_thread(display.stream_table, (table,))

    match.execute_script()




