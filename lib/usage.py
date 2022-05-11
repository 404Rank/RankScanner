import os;
from lib.ColorOut import ColorText
from Config.Conf import config
class usage:
    def __init__(self) -> None:
        pass
    def useArg(*arg) -> None:
        arg = arg[0]
        if '--version' in arg or '-version' in arg:
            print(ColorText.information+"version: %s" % (config.VERSION));
        elif '--help' in arg or '-help' in arg:
            if(os.path.exists("./Others/helper.txt")):
                with open("./Others/helper.txt") as file:
                    #显示帮助文档
                    print(file.read());
            else:
                print(ColorText.warning+"[Rankscanner] %\Others\helper.txt is not exisit!" % __file__);
                print(ColorText.information+"But you can find the help at https://github.com/404Rank/RankScanner");
        elif '--url' in arg or '-url' in arg:
            if '--git' in arg or '-git' in arg:
                print(ColorText.information+"[Rankscanner] .git scanning");
        else:
            print(ColorText.warning+"No arguments named %s" % (" ".join(arg)));

