# -*- coding: utf-8 -*-
import scrapy, re
from scrapy.http import Request
from news.items import NewsItem


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://news.baidu.com/widget?id=LocalNews&ajax=json']
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"}
    ids = ['LocalNews', 'civilnews', 'InternationalNews', 'EnterNews', 'SportNews', 'FinanceNews', 'TechNews',
           'MilitaryNews', 'InternetNews', 'DiscoveryNews', 'LadyNews', 'HealthNews', 'PicWall']

    def parse(self, response):
        for i in self.ids:
            url = "http://news.baidu.com/widget?id=" + i + "&ajax=json"
            yield Request(url, callback=self.parse_next, headers=self.header)

    def parse_next(self, response):
        item = NewsItem()
        page = response.body.decode('unicode_escape')
        # print(page)
        title1 = '"title":"(.*?)"'
        title2 = '"m_title":"(.*?)"'
        link1 = '"url":"(.*?)"'
        link2 = '"m_url":"(.*?)"'
        # print("正在爬取url：" + response.url)
        res = re.compile(link1).findall(page)
        res2 = re.compile(link2).findall(page)
        if len(res)!=0:
            item['title'] = re.compile(title1, re.S).findall(page)
            item['link'] = re.compile(link1, re.S).findall(page)
        elif len(res2)!=0:
            item['title'] = re.compile(title2, re.S).findall(page)
            item['link'] = re.compile(link2, re.S).findall(page)
        print(item["title"])
        print(len(item["title"]))
        print(item["link"])
        print(len(item["link"]))
        yield item
