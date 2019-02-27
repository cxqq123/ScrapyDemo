import pymysql

class MySQLPipeline(object):

    def __init__(self):
        #连接数据库
        self.connect = pymysql.connect(
            host = '127.0.0.1',
            port = 3306,
            db = 'bendibao',
            user = 'root',
            passwd = 'root',
            charset = 'utf8',
            use_unicode = True
        )
        self.cursor = self.connect.cursor()

    def process_item(self,item,spider):
        self.cursor.execute(
            # 纯属python操作mysql知识，不熟悉请恶补
            """insert into app_activity(cname, ctime, address,price ,photo , urlLink)
                       value (%s, %s, %s, %s, %s , %s)""",
            (item['cname'], item['ctime'],item['address'],item['price'],item['photo'],item['urlLink'],)
        )
        #提交sql语句
        self.connect.commit()
        #必须实现返回
        return item