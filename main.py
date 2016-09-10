from UserInterface import MenuItem
from UserInterface import MenuAction

from curses import wrapper
import curses.ascii
import math
import logging


_logger = logging.getLogger(__name__)

def configure_logger():
    logging.basicConfig(level=logging.DEBUG,
                        filename="test",
                        format='%(asctime)s:%(levelname)s:%(filename)s:%(lineno)d:%(message)s')

def main(stdscr):
    """

    :type stdscr: curses window object
    """

    configure_logger()

    _logger.debug("Oh Hai!")

    m = MenuItem('test', 'test')

    menu = {m}

    # Clear screen
    stdscr.clear()

    menu_start_height = math.floor((stdscr.getmaxyx()[0] - len(menu))/2)

    while 1:
            c = stdscr.getch()
            if c == ord('q'):
                _logger.debug("You hit q")
                break  # Exit the while()
            elif c == curses.KEY_HOME:
                _logger.debug("You hit Home")
            else:
                for i in range(0, len(menu)):
                    stdscr.addstr(menu_start_height+i, 0, m.title)
                stdscr.refresh()
                _logger.debug("burp")


    stdscr.getkey()




wrapper(main)
