
from table import Table
from robot import Robot
from match import Match
import _thread
from simulate_LL import SimulatedLL
import display
import time

if __name__ == '__main__':
    ll = SimulatedLL()
    time.sleep(0.2)
    table = Table()
    robot = Robot()




    match = Match(table, robot)

    _thread.start_new_thread(display.stream_table, (table,))



    match.execute_script()




