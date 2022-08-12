from helpers import *
from curses import wrapper


def main(stdscr):
    level = 0
    start_screen(stdscr)

    while True:
        wpm_test(stdscr, level)
        stdscr.addstr(
            3, 0, "You completed the text!\nPress ANY KEY to continue, R to restart this or ESCAPE to exit.")

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break
        elif ord(key) in (114, 82):
            continue
        else:
            level += 1
            continue


if __name__ == "__main__":
    wrapper(main)
