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
            #SVN
            '.svn/entries',
            '.svn/wc.db',
            #HG
            '.hg',
            hostname+".zip" if hostname!= None else "",
            hostname+".rar" if hostname!= None else "",
            hostname+".bak" if hostname!= None else "",
        ] if item!="");
    
    def EditorList(fileName:str) -> list:
        if fileName == "" or fileName is None:
            return [];
        else:
            return list(map(lambda container: container % fileName,[
                ".%s.swp",
                ".%s.swo",
                ".%s.swn",
                "%s~" #gedit Leakage
            ]));
    
    def homePage() -> list:
        '''
        二维数组分类
        后期方便通过对应不同的类型进行嗅探
        '''
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