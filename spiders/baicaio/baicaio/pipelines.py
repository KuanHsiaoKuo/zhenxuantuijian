# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb


# 定义基本的数据库信息
dbuser = 'root'
dbpass = '123456'
dbname = 'blogdb'
dbhost = ''
dbport = ''


# 管道名字可以任意命名，要和settings中的一致
class MySQLStorePipeline(object):
    # 写连接数据库的初始化方法
    def __init__(self):
        self.conn = MySQLdb.connect(
            user=dbuser, passwd=dbpass, db=dbname, host=dbhost, charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                """
                insert into blog_article  select max(id) +1,
                %s,%s,%s,%d,%d,%s,%d,%d
                from blog_article
                """,
                (
                    item['title'][0].encode('utf-8'),
                )
            )
            self.conn.commit()
        except MySQLdb.Error as e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item
