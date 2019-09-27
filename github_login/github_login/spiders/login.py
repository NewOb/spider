# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest
from github_login.items import GithubLoginItem


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/']
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"}
    item = GithubLoginItem()

    # 访问入口
    def start_requests(self):
        return [Request("https://github.com/login", meta={"cookiejar": 1}, callback=self.parse)]

    def parse(self, response):
        # post地址：https://github.com/session
        # 填写表单所需要得相关数据
        data = {
            "login": "854306349@qq.com",
            "password": "1997@lz",
        }
        return [FormRequest.from_response(response,
                                          # 设置cookie信息
                                          meta={"cookiejar": response.meta["cookiejar"]},
                                          # 设置headers模拟浏览器
                                          headers=self.header,
                                          # 设置post表单数据
                                          formdata=data,
                                          # 设置回调函数
                                          callback=self.next,
                                          dont_filter=True
                                          )]

    def next(self, response):
        # 保持cookie继续下一步操作
        print("正在登陆...")
        print([Request("https://github.com", meta={"cookiejar": True}, callback=self.next2)])
        yield Request("https://github.com", meta={"cookiejar": True}, callback=self.next2)

    def next2(self, response):
        print("正在获取数据")
        self.item["name"] = response.xpath("//a[@data-hovercard-type='repository']/@href").extract()
        result = self.item["name"]
        result = list(set(result))
        for i in result:
            print(i+"\n")
