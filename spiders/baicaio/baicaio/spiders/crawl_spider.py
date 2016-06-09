#-*- coding:utf-8 -*-
# 这个爬虫用来自动提取文章列表页面的文章链接接
import pdb
from baicaio.items import BaicaioItem
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class Crawl_Spider(CrawlSpider):
    name = "from_list_spider"
    allowed_domains = ["baicaio.com"]
    start_urls = ['http://www.baicaio.com/page/' + str(n) for n in range(1,4)]
    rules = [
        # 用正则匹配跳转链接
        # Rule(LinkExtractor(allow=('http://www\.baicaio\.com/\?go/[0-9]{1,7}/', )),
        #     callback='parse_jump'),
        Rule(LinkExtractor(allow=('http://www.baicaio.com/20[0-9]{2}/[0-9]{1,2}/[0-9]{1,2}/.*\.html',)),callback='parse_item'),
    ]

    def parse_jump(self,response):
        pass


    def parse_item(self,response):
        item = BaicaioItem()
        title = response.xpath(
            '//*[@id="content"]/ul/li/h1/a/@title'
            ).extract()
        item["title"] = title[0]
        yield item

