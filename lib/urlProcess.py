'''
@Author:404Rank
'''
from dataclasses import replace
from urlobject import URLObject;
class urlObject:
    def __init__(self,url) -> None:
        url = url.replace("\\","/");
        self.url = url;
        self.urlObj = URLObject(url);
        #主机处理
        if self.urlObj.scheme == None or self.urlObj.scheme == "":
            self.url = "http://"+self.url;
        self.urlObj = URLObject(self.url);
        obj = self.urlObj
        if self.urlObj.port == None or self.urlObj.port == "":
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
            mainAddr = mainAddr+":"+self.port
        return mainAddr;

    def get_list_name(self)-> list :
        '''
        获取目录名
        0级目录:/
        '''
        deepList = list(item for item in self.path.split("/") if item !="");
        deepList.insert(0,"/");
        return deepList;
