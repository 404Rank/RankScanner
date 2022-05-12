'''
@Author:404Rank
'''
from urlobject import URLObject;
class urlObject:
    def __init__(self,url) -> None:
        self.url = url;
        self.urlObj = URLObject(url);

        if self.urlObj.scheme == None or self.urlObj.scheme == "":
            url = "http://"+url;
        obj = URLObject(url);
        if self.urlObj.port == None or self.urlObj.port == "":
            self.port = "";
        else:
            self.port = obj.port;
        self.protocal =  obj.scheme;
        self.host = obj.hostname;
        self.path = obj.path;
        self.query = obj.query;