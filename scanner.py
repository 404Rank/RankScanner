#!/usr/bin/python 
'''
@Author: 404Rank
'''
import sys
from lib.usage import usage
import lib.draw as draw
if __name__ == "__main__":
    if len(sys.argv) > 1:
        argvs = sys.argv[1:];
        usage.useArg(argvs);
    else:
        print(draw.Text);