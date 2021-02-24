import sys
import os
import getopt


_inputfile_path = ""
measurements = {}

def help():
    print("python files.py -i <inputfile> [-h]")

def parse(argv):
    print("Number of arguments: ", len(sys.argv), "arguments")
    print("Argument List: ", str(sys.argv))

    try:
        opts, args = getopt.getopt(argv, "hi:", ["ifile"])
    except getopt.GetoptError:
        help()
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            help()
        elif opt in ("-i", "--ifile"):
            _inputfile_path = arg
        else:
            help()
            sys.exit(2)
    if not os.path.exists(_inputfile_path):
        help()
        sys.exit(2)
    print("Path is ", _inputfile_path)

def load():
    with open(_inputfile_path, 'r') as file:
        pass

if __name__ == "__main__":
    parse(sys.argv[1:])
