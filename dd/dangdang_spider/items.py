# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 商品名
    title = scrapy.Field()
    # 商品链接
    link = scrapy.Field()
    # 评论数
    comment = scrapy.Field()
