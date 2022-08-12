import curses
import time
import json
from colors import *


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr, target, current, str_line=0):
    stdscr.addstr(target)
    for i, char in enumerate(current):
        try:
            correct_char = target[i]
            color = correct
            if char != correct_char:
                color = incorrect
            stdscr.addstr(str_line, i, char, color)
        except curses.error:
            pass


def wpm_test(stdscr, level):
    target_text = None
    with open("text.json", "r") as f:
        json_load = json.load(f)
        try:
            target_text = json_load[level]["text"]
        except:
            pass

    current_text = []

    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        if target_text == None:
            stdscr.nodelay(False)
            stdscr.clear()
            stdscr.addstr("\nCongrats! You have completed all the levels")
            stdscr.addstr(3, 25, "PRESS ESC")
            stdscr.getkey()
            break

        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text)

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            stdscr.addstr(
                1, 0, f"Speed: {wpm}wpm   -   Duration: {round(time_elapsed, 2)}s")
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            if ord(key) == 27:
                break
            if key in ("KEY_ENTER", "\n", "\x0D"):
                continue
            else:
                current_text.append(key)

        stdscr.refresh()
