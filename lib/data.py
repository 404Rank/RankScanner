'''
@Author: 404Rank
@Desc: data;
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

    def basicList(hostname="") -> list:
        return list(item for item in [
            'robots.txt',
            '.htaccess',
            'README.md',
            'readme.md',
            'www.zip',
            'www.rar',
            'www.tar.gz',
            hostname+".zip" if hostname!="" else "",
            hostname+".rar" if hostname!="" else ""
        ] if item!="");
    

    