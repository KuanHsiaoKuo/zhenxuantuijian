import json
import os


# 用Python获得一些有关系统的各种信息
# 默认设置了DJANGO_SETTINGS_MODULE，所以任何一个django project中的*.py文件都能够正常的使用项目中的数据模型操作。
# 所以这个要在导入模型之前声明
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zhenxuantuijian.settings")


from blog.models import Article
fin = open('baicaio_items.json', 'r')
s = json.load(fin)
# print (type(s)) # 最外面是数组，对应python的list
article_list = []
for line in s:
    # print (type(line)) # 里面每条记录其实就是字典
    # print (line['title'])
    # 这里是一次一次的生成对象，效率不够
    # article = Article.objects.create(title = line['title'])
    # 我们可以先生成对象，然后后面批量存入数据库
    article = Article(title=line['title'])
    article_list.append(article_list)
fin.close()

# 这是批量通过orm存入数据库
Article.objects.bulk_create(article_list)