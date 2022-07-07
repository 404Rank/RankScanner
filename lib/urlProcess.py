'''
@Author:404Rank
'''
import sys,re;
from lib.ColorOut import ColorText
try:
    from urlobject import URLObject;
except:
    print(ColorText.warning + "You don't have the urlobject library yet, but you can install it with this command: $ pip install -r requirement.txt");
    sys.exit();

class urlObject:
    def __init__(self,url) -> None:
        url = url.replace("\\","/");
        self.url = url;
        self.urlObj = URLObject(url);
        #主机处理
        if self.urlObj.scheme is None or self.urlObj.scheme == "":
            self.url = "http://"+self.url;
            
        self.urlObj = URLObject(self.url);
        obj = self.urlObj
        if self.urlObj.port is None:
            self.port = "";
        else:
            self.port = obj.port;
        self.protocal =  obj.scheme;
        self.host = obj.hostname;
        self.path = obj.path;
        self.query = obj.query;
    def getMainAddr(self) -> str:
        '''
        获取可访问主机地址，包括端口
        '''
        mainAddr = "%s://%s" % (self.protocal,self.host);
        if self.port != "":
            mainAddr = mainAddr+":"+str(self.port);
        return mainAddr;

    def get_list_name(self)-> list :
        '''0
        获取目录名
        0级目录:/
        '''
        deepList = list(item for item in self.path.split("/") if item !="");
        deepList.insert(0,"/");
        return deepList;

    def isURL(self,url:str) -> bool:
        reg = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://  ftp or ftps
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE
        );
        return (re.match(reg,url) is not None)