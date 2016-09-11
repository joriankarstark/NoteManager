from UserInterface import MenuItem
from UserInterface import MenuAction

from curses import wrapper
import curses.ascii
import math
import logging


_logger = logging.getLogger(__name__)

def configure_logger():
    """
    setup basic logger config
    """
    logging.basicConfig(level=logging.DEBUG,
                        filename="test",
                        format='%(asctime)s:%(levelname)s:%(filename)s:%(lineno)d:%(message)s')

def show_menu(stdscr, menu):
    """
    :type stdscr: curses window object
    """

    menu_start_height = math.floor((stdscr.getmaxyx()[0] - len(menu))/2)

    menu_item_number = 0
    for menu_item in menu:
        stdscr.addstr(menu_start_height+menu_item_number, 0, menu_item.title)
        menu_item_number += 1
    stdscr.refresh()

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
    show_menu(stdscr, menu)

    while 1:
            c = stdscr.getch()
            if c == ord('q'):
                _logger.debug("You hit q")
                break  # Exit the while()
            elif c == curses.KEY_HOME:
                _logger.debug("You hit Home")
            else:
                _logger.debug("burp")


    #stdscr.getkey()




wrapper(main)
