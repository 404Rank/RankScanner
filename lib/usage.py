import os;
import difflib;
from Config.Conf import config
from lib.ColorOut import ColorText
from lib.Core import gitInfo
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
#--------------------------------------------------------------------------------------------------------------------
        elif '--url' in arg or '-url' in arg:
            # url
            match = difflib.get_close_matches('-url',arg,1,cutoff=0.7)[0];
            Index = arg.index(match)
            require = arg[Index:Index+2];
            if (len(require) == 2):
                gitScan = gitInfo(require[1]);
                gitScan.start();
            #only scann git info
            if '--git' in arg or '-git' in arg:
                print(ColorText.information+"[Rankscanner] .git scanning");
        
        else:
            print(ColorText.warning+"No arguments named %s" % (" ".join(arg)));

