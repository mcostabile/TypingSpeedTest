import curses

curses.initscr()
curses.start_color()
curses.use_default_colors()

curses.init_pair(1, curses.COLOR_GREEN, 234)
correct = curses.color_pair(1)

curses.init_pair(2, curses.COLOR_RED, 234)
incorrect = curses.color_pair(2)

curses.init_pair(3, curses.COLOR_GREEN, 4)
corrected = curses.color_pair(3)
