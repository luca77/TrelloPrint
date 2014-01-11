#!/usr/bin/python3

import os

import argparse
import json

from board import Board


RELEASE = "0.3pre"

TEMP_FILE_NAME = "/tmp/tp.md"


def main():
    parser = argparse.ArgumentParser(description='Print Trello.com JSON file')
    parser.add_argument('-f', '--format', choices=["text", "markdown", "html"],
         default="markdown")
    parser.add_argument('source', metavar="json_file")
    parser.add_argument('-v', '--version', action='version',
        version='TrelloPrint ' + RELEASE)
    args = parser.parse_args()

    filename = args.source

    f = open(filename)
    data = json.load(f)
    f.close()

    b = Board(data)
    if (args.format == "text"):
        print(b)
        exit

    md_string = b.get_md()
    if (args.format == "markdown"):
        print(md_string)
        exit

    if (args.format == "html"):
        temp_fd = open(TEMP_FILE_NAME, "w")
        temp_fd.write(md_string)
        temp_fd.close()
        os.system("markdown " + TEMP_FILE_NAME)
        os.remove(TEMP_FILE_NAME)


if __name__ == "__main__":
    main()
