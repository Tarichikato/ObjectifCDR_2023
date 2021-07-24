
from table import Table
from robot import Robot
from match import Match
import _thread
from simulate_LL import SimulatedLL
import display

if __name__ == '__main__':
    table = Table()
    robot = Robot()
    ll = SimulatedLL()



    match = Match(table, robot)

    _thread.start_new_thread(match.execute_script, ())

    display.stream_table(table)




