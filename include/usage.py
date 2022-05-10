from genericpath import exists
class usage:
    def __init__(self) -> None:
        pass
    def useArg(*arg) -> None:
        arg = arg[0]
        if '--version' in arg or '-version' in arg:
            print("[Rankscanner] version is %s" % ("1.0.0"));
        elif '--help' in arg or '-help' in arg:
            if(exists("./Others/helper.txt")):
                with open("./Others/helper.txt") as file:
                    print(file.read());
        elif '--url' in arg or '-url' in arg:
            if '--git' in arg or '-git' in arg:
                print("[Rankscanner] .git scanning");
        else:
            print("No arguments named %s" % (" ".join(arg)));