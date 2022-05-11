from Config.Conf import config
from lib.data import DataSet;
from lib.ColorOut import ColorText;
import urllib3;
from urlobject import URLObject;
class gitInfo:
    def __init__(self,url) -> None:
        self.url = url;
        self.urlObj = URLObject(url);
        self.http = urllib3.PoolManager();
    def start(self) -> None:
        print(ColorText.information + "start to git scann");
        #send request
        require = self.http.request(
            "GET",
            self.url
        );
        statusCode = require.status;
        if statusCode == 200:
            print(ColorText.information+"Request succeeded!");
            self.basciLeakage();
            self.GitLeakage();
        else:
            print(ColorText.warning + "The website could require and the status is %s" % str(statusCode));
    def basciLeakage(self) -> None:
        url = self.url;
        urlObj = self.urlObj;
        basciList = DataSet.basicList(urlObj.hostname);
        target = "%s://%s:%s/" % (urlObj.scheme,urlObj.hostname,str(urlObj.port));
        for i in basciList:
            signals = target + i;
            print(ColorText.information + "is testing "+signals);
            require = self.http.request(
                "GET",
                signals
            )
            if(require.status == 200):
                print(ColorText.find + "This url maybe A Leakage:   " + signals);

    def GitLeakage(self) -> None:
        pass;
