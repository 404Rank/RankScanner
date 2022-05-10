import sys
from include.usage import usage
if __name__ == "__main__":
    if len(sys.argv) > 1:
        argvs = sys.argv[1:];
        usage.useArg(argvs);
   
