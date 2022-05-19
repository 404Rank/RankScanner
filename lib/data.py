'''
@Author: 404Rank
@Desc: 目录遍历
'''
class DataSet:
    def gitList() -> list:
        return list(map(lambda item: ".git/"+item,[
            'config/',
            'HEAD',
            "ORIG_HEAD",
            "FETCH_HEAD",
            'description',
            "index",
            'hooks/',
            'info/',
            'info/exclude',
            'info/refs',
            "objects/",
            "refs/",
        ]));

    def basicList(hostname=None) -> list:
        return list(item for item in [
            'robots.txt',
            '.htaccess',
            'README.md',
            'readme.md',
            'www.zip',
            'www.rar',
            'www.tar.gz',
            hostname+".zip" if hostname!= None else "",
            hostname+".rar" if hostname!= None else "",
            hostname+".bak" if hostname!= None else "",
        ] if item!="");
    
    def vimList(fileName:str) -> list:
        if fileName == "" or fileName is None:
            return [];
        else:
            return list(map(lambda container: container % fileName,[
                ".%s.swp",
                ".%s.swo",
                ".%s.swn",
                "%s~" #gedit backup
            ]));
    
    def homePage() -> list:
        home = [
            "index",
            "main",
            "www",
            "default",
            "wrapper",
            "page",
            "container",
        ];homeList = [];
        for i in ['php','asp','aspx','jsp']:
            homeList.append(list(map(lambda name: name+"."+i,home)));
        return homeList;