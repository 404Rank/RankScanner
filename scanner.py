import sys
from include.usage import usage
if __name__ == "__main__":
    argvs = sys.argv[1:];
    usage.useArg(argvs);
    