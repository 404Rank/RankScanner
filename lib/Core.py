from sys import prefix
from Config.Conf import config
from lib.data import DataSet;
from lib.ColorOut import ColorText;
from lib.urlProcess import urlObject;
import urllib3;
import re;
class appCore:
    def __init__(self,url) -> None:
        self.url = url;
        self.urlObj = urlObject(url);
        self.http = urllib3.PoolManager();
        self.res = {
            "finder":[],
            "maybe":[]
        };
        self.slash = re.compile("[\/]{1,}",re.IGNORECASE);
    def start(self) -> None:
        #send request
        try:
            require = self.http.request(
                "GET",
                self.url,
                timeout=config.CONN_WAIT_TIME
            );
        except:
            print(ColorText.warning + "connecting %s faild!" % (self.url));
            return;
        statusCode = require.status;
        if statusCode == 200:
            print(ColorText.information+"Request succeeded! Start to scan");
            tarList = self.urlObj.get_list_name();
            self.basciLeakage(tarList);
            self.GitLeakage(tarList);
            self.res_out_put();
        else:
            print(ColorText.warning + "The website couldn't request and the status code is %s" % str(statusCode));

    #core
    def basciLeakage(self,tarList) -> None:
        urlObj = self.urlObj;
        mainAddr = urlObj.getMainAddr();
        print(tarList,mainAddr);
        for deep in range(0,len(tarList)):
            prefix = tarList[deep]
            if(prefix == "/"):
                basciList = DataSet.basicList(urlObj.host);
            else:
                basciList = DataSet.basicList(prefix);
            for i in basciList:
                signals = self.slash.sub("/",("/".join(tarList[0:deep]) +"/"+ i));
                signals = mainAddr + signals;
                print(ColorText.information + "Testing "+signals);
                try:
                    require = self.http.request(
                        "GET",
                        signals,
                        timeout = config.CONN_WAIT_TIME
                    )
                except:
                    print(ColorText.warning + "connect faild!");
                    return;
                if(require.status == 200):
                    self.res['finder'].append(ColorText.find + "200 - " + "This url maybe A Leakage: " + signals)
                elif(require.status == 403 or require.status == 304):
                    self.res['maybe'].append(ColorText.maybe + "%s - "%(str(require.status)) + "This url maybe A Leakage: " + signals)
        #basic end
        
    def GitLeakage(self,tarList) -> None:
        urlObj = self.urlObj;
        gitList = DataSet.gitList();
        mainAddr = self.urlObj.getMainAddr();
        pass;

    def res_out_put(self) -> bool:
        for item in self.res.values():
            if(len(item)>0):
                print(ColorText.block);
                for out in item:
                    print(out);
        return True;
            