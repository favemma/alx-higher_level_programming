#!/usr/bin/python3
import sys


def main(*argv):

    i = 0

    a = len(sys.argv) - 1

    if a == 1:

        print("{:d} argument:".format(a))

    elif a == 0:

        print("{:d} arguments.".format(a))

    else:

        print("{:d} arguments:".format(a))

    for args in sys.argv:

        if (i != 0):

            print("{}: {}".format(i, args))

        i += 1


if __name__ == "__main__":

    main()
