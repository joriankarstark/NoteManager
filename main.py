from UserInterface import MenuItem
from UserInterface import MenuAction

from curses import wrapper
import math

def main(stdscr):
    """

    :type stdscr: curses window object
    """

    m = MenuItem('test', 'test')

    menu = {m}

    # Clear screen
    stdscr.clear()

    menu_start_height = math.floor((stdscr.getmaxyx()[0] - len(menu))/2)

    for i in range(0, len(menu)):
        stdscr.addstr(menu_start_height+i, 0, m.title)


    stdscr.refresh()
    stdscr.getkey()





wrapper(main)
