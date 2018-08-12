#!/usr/bin/env python
import sys


def usage():
    print('Usage: schnitzel [filename]')


def main(argv):
    if len(argv) != 2:
        usage()

    filename = argv[1]
    file = open(filename)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    main(sys.argv)
