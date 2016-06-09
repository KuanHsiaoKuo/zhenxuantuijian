#-*- coding:utf-8 -*-
import scrapy
import pdb

class Tutorial_Spider(scrapy.spiders.Spider):
    # 用于区别Spider。
    # 该名字必须是唯一的，您不可以为不同的Spider设定相同的名字。
    name = "baicaio_tutorial"
    allowed_domains = ['baicaio.com']
    # 包含了Spider在启动时进行爬取的url列表。
    # 因此，第一个被获取到的页面将是其中之一。
    # 后续的URL则从初始的URL获取到的数据中提取。   
    start_urls = [
        "http://www.baicaio.com/2016/06/09/180093.html",
    ]
    # 是spider的一个方法。 被调用时，每个初始URL完成下载后生成的 Response
    # 对象将会作为唯一的参数传递给该函数。 该方法负责解析返回的数据(response
    # data)，提取数据(生成item)以及生成需要进一步处理的URL的 Request 对象。
    def parse(self,response):
        title = response.xpath(
            '//*[@id="content"]/ul/li/h1/a/@title'
            ).extract()
        print title  # 打印的是列表，不显示中文
        print title[0] #直接打印中文
