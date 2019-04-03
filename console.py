'''
TO DO

    Hold up array of 5 messages

'''

import signal, time, os
from os import system

class Console(object):

    l_end = ' > '
    l_beg = ' '
    l_ind = ' • '
    l_imp = ' • '

    c_height = 5
    c_col_lenth, c_row_lenth = os.get_terminal_size(0)
    c_block_history = 40
    c_game = []
    c_block = [' '] * c_block_history

    def __init__(self):
        # window resize hanlder
        signal.signal(signal.SIGWINCH, self.resize_handler)

    def resize_handler(self, signum, frame):
        self.cls()
        self.c_col_lenth, self.c_row_lenth = os.get_terminal_size(0)
        self.print_console()

    # methodes

    def spacer(self):
        return print("-" * self.c_col_lenth)

    def cls(self):
        return print("\n" * self.c_row_lenth)

    # clears game

    def cls_game(self):
        self.c_game = []

    # history flood prevention

    def check_history_length(self):

        while not len(self.c_block) < self.c_block_history:
            self.c_block.pop(0)

    # utilities

    def input(self, message=''):
        val = input(f" {message}{self.l_end}")
        self.cls()
        self.print_console()
        return val

    def print(self, message, console=0):
        self.cls()
        self.check_history_length()

        if console:
            self.c_block.append(message)
        else:
            self.c_game.append(message)

        self.print_game()
        self.print_console()
        time.sleep(.5)

    def p_continue(self):
        self.input("< CONTIUNE")
        self.cls_game()

    def print_game(self):
        for i in self.c_game:
            print(self.l_beg, i)

    def print_console(self):

        self.spacer()

        for i in self.c_block[:-self.c_height-1:-1]:
            print(self.l_ind, i)

        self.spacer()
