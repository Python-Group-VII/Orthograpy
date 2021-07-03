#! /usr/bin/env python3

import sys

from file_reading import file_reading


def main():
    print(file_reading(sys.argv[1]))

if __name__ == '__main__':
    main();
