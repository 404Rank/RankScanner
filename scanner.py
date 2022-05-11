#! /usr/bin/python
'''
@Author: 404Rank
'''
import sys
from lib.usage import usage
from lib.data import *
from lib.ColorOut import ColorText
if __name__ == "__main__":
    if len(sys.argv) > 1:
        argvs = sys.argv[1:];
        usage.useArg(argvs);