import sys
import os
import getopt
import re


_inputfile_path = ""
measurements = {}

def file_handling():
    parse(sys.argv[1:])
    load()

def help():
    print("This is a help message. Run the program as follows:")
    print("python(3) files.py -i <inputfile> [-h]")

def parse(argv):
    global _inputfile_path
    try:
        opts, args = getopt.getopt(argv, "hi:", ["ifile"])
    except getopt.GetoptError:
        help()
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            help()
            sys.exit(2)
        elif opt in ("-i", "--ifile"):
            _inputfile_path = arg
        else:
            help()
            sys.exit(2)
    if not os.path.exists(_inputfile_path):
        help()
        sys.exit(2)
    print("Path is valid: " + str(_inputfile_path) + '\n')

def load():
    global measurements
    with open(_inputfile_path, 'r') as file:
        for line in file:
            list_line = (line.rstrip()).split(' ')
            if len(list_line) < 2:
                continue
            elif re.match(r'^-?\d+(?:\.\d+)$', list_line[0]) is None:
                continue
            angle = float(list_line[0])
            distance = float(list_line[1])
            measurements[angle] = distance
