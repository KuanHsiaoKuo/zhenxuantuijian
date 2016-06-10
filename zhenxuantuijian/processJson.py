import json
import os


# 用Python获得一些有关系统的各种信息
# 默认设置了DJANGO_SETTINGS_MODULE，所以任何一个django project中的*.py文件都能够正常的使用项目中的数据模型操作。
# 所以这个要在导入模型之前声明
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zhenxuantuijian.settings")


from blog.models import Article
fin = open('baicaio_items.json', 'r')
s = json.load(fin)
print (type(s)) # 最外面是数组，对应python的list
for line in s:
    print (type(line)) # 里面每条记录其实就是字典
    print (line['title'])