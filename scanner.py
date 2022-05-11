#! /usr/bin/python
'''
@Author: 404Rank
'''
import sys
from lib.usage import usage
from lib.draw import Draw
if __name__ == "__main__":
    if len(sys.argv) > 1:
        argvs = sys.argv[1:];
        usage.useArg(argvs);
    else:
        print(Draw.toCharImage("./Others/img/logo.png"));