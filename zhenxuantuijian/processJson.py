import json
import os
# from blog.models import Article
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zhenxuantuijian.settings")
fin = open('baicaio_items.json', 'r')
s = json.load(fin)
print (type(s)) # 最外面是数组，对应python的list
for line in s:
    print (type(line)) # 里面每条记录其实就是字典
    print (line)