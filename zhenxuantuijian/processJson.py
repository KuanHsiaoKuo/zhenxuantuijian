import json

fin = open('baicaio_items.json', 'r')
# for eachline in fin:
    # line = eachline.strip().decode('utf-8')
    # line = eachline.strip(',')
    # print (type(line))
    # print ('内容：' + line)

s = json.load(fin)
print (type(s))  # 获得list对象
print (len(s))
print (s)