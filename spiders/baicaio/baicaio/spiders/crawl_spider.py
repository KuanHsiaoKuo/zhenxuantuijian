#-*- coding:utf-8 -*-
# 这个爬虫用来自动提取文章列表页面的文章链接接
import pdb
from baicaio.items import BaicaioItem
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import random
import re

class Crawl_Spider(CrawlSpider):
    name = "from_list_spider"
    allowed_domains = ["baicaio.com"]
    # start_urls = ['http://www.baicaio.com/page/' + str(n) for n in range(1,4)]
    start_urls = ['http://www.baicaio.com']
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
        item["title"] = title[0].encode('utf-8')
        desc = \
            response.xpath('//*[@id="content"]/ul/li/div[3]/p[1]').extract()
        desc[0] = desc[0].encode('utf-8')
        if len(desc[0]) > 50 : desc[0] = desc[0][0:49] + '...'
        item["desc"] = desc[0]
        content = \
            response.xpath('//*[@id="content"]/ul/li/div[3]/p').extract()
        item['content'] = content[0].encode('utf-8')
        item["click_count"] = random.randint(0,20)
        item["is_recommend"] = random.choice([0,1])
        # 从url中取出发布日期
        date = '-'.join(response.url.split('/')[3:6])
        # 从网页中获取发布时间
        time = \
            response.xpath('//*[@id="content"]/ul/li/div[1]/div[2]').extract()[0]
        time = re.findall("(?<=>).*(?=<)",time)[0]
        publish_date = [date,time]
        item["date_publish"] = ' '.join(publish_date)
        item["user_id"] = random.randint(1,3)
        item["category_id"] = random.randint(1,2)
        yield item

