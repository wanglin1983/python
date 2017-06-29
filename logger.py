#!/usr/bin/python

NONE="\033[0m"
BLACK="\033[0;30m"
DARK_GRAY="\033[1;30m"
BLUE="\033[0;34m"
LIGHT_BLUE="\033[1;34m"
GREEN="\033[0;32m"
LIGHT_GREEN="\033[1;32m"
CYAN="\033[0;36m"
LIGHT_CYAN="\033[1;36m"
RED="\033[0;31m"
LIGHT_RED="\033[1;31m"
PURPLE="\033[0;35m"
LIGHT_PURPLE="\033[1;35m"
BROWN="\033[0;33m"
YELLOW="\033[1;33m"
LIGHT_GRAY="\033[0;37m"
WHITE="\033[1;37m"

def cprint(color, string):
    print color + string + NONE 

def info(string):
    cprint(YELLOW, string)

def error(string):
    cprint(RED, string)

def debug(string):
    cprint(LIGHT_GREEN, string)

def print_color_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')
