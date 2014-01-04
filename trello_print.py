#!/usr/bin/python3

import argparse
import json
#from pprint import pprint

from board import Board


release = "0.2pre"


def main():
    parser = argparse.ArgumentParser(description='Print Trello.com JSON file')
    parser.add_argument('-f', '--format', choices=["text", "markdown", "html"],
         default="markdown")
    parser.add_argument('source', metavar="json_file")
    parser.add_argument('-v', '--version', action='version',
        version='TrelloPrint ' + release)
    args = parser.parse_args()

    filename = args.source

    f = open(filename)
    data = json.load(f)
    f.close()

    b = Board(data)
    if (args.format == "text"):
        print(b)

    md_string = b.get_md()
    if (args.format == "markdown"):
        print(md_string)

if __name__ == "__main__":
    main()
