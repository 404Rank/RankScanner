from genericpath import exists


class usage:
    def __init__(self) -> None:
        pass
    def useArg(*arg) -> None:
        arg = arg[0]
        if '--version' in arg or '-version' in arg:
            print("[Rankscanner] version is %s" % ("1.0.0"));
        elif '--help' in arg or '-help' in arg:
            if(exists("./README.md")):
                with open("./README.md") as file:
                    print(file.read());
        elif '--git' in arg or '-git' in arg:
            print("[Rankscanner] .git scanning");