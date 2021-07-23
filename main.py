
from table import Table
from robot import Robot
from match import Match
from simulate_LL import init_simulated_LL
import display as display

if __name__ == '__main__':
    table = Table()
    robot = Robot()
    init_simulated_LL()

    match = Match(table, robot)

    match.execute_script()
    while True:
        pass



