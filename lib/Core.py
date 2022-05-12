from socket import timeout
from Config.Conf import config
from lib.data import DataSet;
from lib.ColorOut import ColorText;
from lib.urlProcess import urlObject;
import urllib3;
class gitInfo:
    def __init__(self,url) -> None:
        self.url = url;
        self.urlObj = urlObject(url);
        self.http = urllib3.PoolManager();
    def start(self) -> None:
        print(ColorText.information + "start to git scann");
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
            print(ColorText.information+"Request succeeded!");
            self.basciLeakage();
            self.GitLeakage();
        else:
            print(ColorText.warning + "The website couldn't request and the status code is %s" % str(statusCode));

    #core
    def basciLeakage(self) -> None:
        urlObj = self.urlObj;
        basciList = DataSet.basicList(urlObj.host);
        target = "%s://%s" % (urlObj.protocal,urlObj.host);
        if urlObj.port != "":
            target = target+":"+urlObj.port
        target += "/"
        res = {
            "finder":[],
            "maybe":[]
        };
        for i in basciList:
            signals = target + i;
            print(ColorText.information + "is testing "+signals);
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
                res['finder'].append(ColorText.find + "200 - " + "This url maybe A Leakage: " + signals)
            elif(require.status == 403):
                res['maybe'].append(ColorText.maybe + "403 - " + "This url maybe A Leakage: " + signals)
        #basic end
        #basci res output
        for item in res.values():
            if(len(item)>0):
                print(ColorText.block);
                for out in item:
                    print(out)
    def GitLeakage(self) -> None:
        pass;

            