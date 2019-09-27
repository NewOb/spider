# -*- coding: utf-8 -*-
import scrapy
from dangdang_spider.items import DangdangSpiderItem
from scrapy.http import Request

class DdSpider(scrapy.Spider):
    name = 'dd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cid10010336.html']
    def parse(self, response):
        item=DangdangSpiderItem()
        item["title"] = response.xpath("//a[@name='itemlist-picture']/@title").extract()
        item["link"] = response.xpath("//a[@name='itemlist-picture']/@href").extract()
        item["comment"] = response.xpath("//a[@name='itemlist-review']/text()").extract()
        # print(item["link"])
        yield item
        for i in range(2,101):
            url = "http://category.dangdang.com/pg"+str(i)+"-cid10010336.html"
            if Request(url,callback=self.parse):
                yield Request(url,callback=self.parse)
            else:
                print("爬取结束")
                break