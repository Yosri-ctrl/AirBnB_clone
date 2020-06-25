#!/usr/bin/python3
import itertools
from os import sys

def user_input():
    for arg in itertools.count():
        try:
            yield arg, input('[%s]: ' % arg)
        except KeyboardInterrupt:
            pass
        except EOFError:
            break

def main():
    for arg, input in user_input():
        pass

if __name__ == '__main__':
    main()