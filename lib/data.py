'''
@Author: 404Rank
@Desc: 目录遍历
'''
class DataSet:
    def gitList() -> list:
        return [
            'config/',
            'HEAD/',
            'description/',
            'hooks/',
            'info/',
            'info/exclude',
            'info/refs'
        ];

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
            hostname+".rar" if hostname!= None else ""
        ] if item!="");
    

    