
from table import Table
from robot import Robot
from match import Match
import display as display

if __name__ == '__main__':
    table = Table()
    robot = Robot()

    match = Match(table, robot)

    while True:
        display.show(table)



