# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaicaioItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 文章标题
    # callback_link = scrapy.Field()  # 抓取网址
    # affiliate_link = scrapy.Field() #  返利链接
    desc = scrapy.Field() # 文章描述
    content = scrapy.Field() # 文章内容
    click_count = scrapy.Field()
    is_recommend = scrapy.Field()
    date_publish = scrapy.Field()
    user = scrapy.Field()
    category_id = scrapy.Field()
    user_id = scrapy.Field()