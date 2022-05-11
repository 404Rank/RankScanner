#! /usr/bin/python
'''
@Author: 404Rank
'''
import sys
from lib.usage import usage
if __name__ == "__main__":
    print(sys.argv);
    if len(sys.argv) > 1:
        argvs = sys.argv[1:];
        
        usage.useArg(argvs);
    