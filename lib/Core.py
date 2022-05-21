from Config.Conf import config
from lib.data import DataSet;
from lib.ColorOut import ColorText;
from lib.urlProcess import urlObject;
import re,sys;
try:
    import urllib3;
except:
    print(ColorText.warning + "You don't have the urllib3 library yet, but you can install it with this command: $ pip install -r requirement.txt");
    sys.exit();

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
            print(ColorText.information+"Request success and Start to scan");
            tarList = self.urlObj.get_list_name();
            #test
            self.BasciLeakage(tarList);
            self.GitLeakage(tarList);
            self.EditorLeakage(tarList);
            self.res_out_put();
        else:
            print(ColorText.warning + "The website couldn't request and the status code is %s" % str(statusCode));

    #core tarList: 路径，且索引越高，目录越深
    def BasciLeakage(self,tarList) -> None:
        urlObj = self.urlObj;
        mainAddr = urlObj.getMainAddr();
        for deep in range(0,len(tarList)):
            prefix = tarList[deep]
            if(prefix == "/"):
                basciList = DataSet.basicList(urlObj.host);
            else:
                basciList = DataSet.basicList(prefix);
            for i in basciList:
                signals = self.slash.sub("/",("/".join(tarList[0:deep]) +"/"+ i));
                target = mainAddr + signals;
                statusCode = self.Require(target);
                if(statusCode == 200):
                    self.res['finder'].append(ColorText.find + "200 - " + "This url is a BasicLeakage: " + target)
                elif(statusCode == 403 or statusCode == 304):
                    self.res['maybe'].append(ColorText.maybe + "%s - "%(str(statusCode)) + "This url maybe A BasicLeakage: " + target)
        #basic end

    def GitLeakage(self,tarList) -> None:
        GitList = DataSet.gitList();
        urlObj = self.urlObj;
        mainAddr = urlObj.getMainAddr();
        for deep in range(0,len(tarList)):
            for add in GitList:
                target = mainAddr + self.slash.sub("/",("/".join(tarList[0:deep]) +"/"+ add));
                statusCode = self.Require(target);
                if(statusCode == 200):
                    self.res['finder'].append(ColorText.find + '200 - '+"This url is a GitLeakage: "+target);
                elif(statusCode == 403 or statusCode == 304):
                    self.res['maybe'].append(ColorText.maybe + '%s - '%(str(statusCode)) + "This url may be a GitLeakage: " + target);
        #Git end

    def EditorLeakage(self,tarList) -> None:
        url = self.url;
        isFile = re.compile(".*\.[html|php|jsp|jspx]*$",re.IGNORECASE);
        editorList = [];
        if isFile.match(tarList[-1]) is None:
            if isFile.match(tarList[-2]) is None:
                return;
            else:
                file = tarList[-2];
                editorList = DataSet.EditorList(file);
                tarList = tarList[0:-2]
        else:
            file = tarList[-1];
            editorList = DataSet.EditorList(file);
            tarList = tarList[0:-1]
        if len(editorList) > 0:
            target = self.urlObj.getMainAddr() + "".join(tarList);
            if tarList[-1] != "/":
                    target += "/";
            for i in editorList:
                status = self.Require(target+i);
                if status == 200:
                    self.res['finder'].append(ColorText.find + '200 - '+"This url is a EditorLeakage: "+target);

    def homePageSniff(self,tarList) -> None:
        pass;

    def res_out_put(self) -> bool:
        for item in self.res.keys():
            value = self.res[item]
            if(len(value)>0):
                value = self.res[item] = list(set(value));
                print(ColorText.block);
                for out in value:
                    print(out);
        return True;

    def Require(self,target) -> int:
        print(ColorText.information + "Trying "+target);
        try:
            require = self.http.request(
                "GET",
                target,
                timeout = config.CONN_WAIT_TIME
            );
            return require.status;
        except:
            print(ColorText.warning + "connect faild!");
            return -1;