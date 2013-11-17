#!/usr/bin/python

import sys
import os
import os.path
import argparse
import json
#from pprint import pprint

from board import Board


def main():
    parser = argparse.ArgumentParser(description='Print Trello.com JSON file')
    parser.add_argument('source', metavar="source file")
    args = parser.parse_args()

    filename = args.source

    f = open(filename)
    data = json.load(f)
    f.close()

    b = Board(data)
    b.print_me()


if __name__ == "__main__":
    main()
