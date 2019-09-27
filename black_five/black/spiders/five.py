# -*- coding: utf-8 -*-
import scrapy
from black.items import BlackItem
import urllib.request,re,time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class FiveSpider(scrapy.Spider):
    name = 'five'
    allowed_domains = ['qq.com']
    start_urls = ['https://ac.qq.com/ComicView/index/id/540929/cid/106']
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(start_urls[0])
    for i in range(20):
        js = 'window.scrollTo(0,1080)'
        driver.execute_async_script(js)
        time.sleep(2)
    driver.get_screenshot_as_file("E:\\web截图\\1.jpg")
    # page = driver.page_source.encode('utf-8')
    # print(page)
    driver.close()

    def parse(self, response):
        # next_url = response.xpath('//ul[@id="ctrl_list"]/li/a/@href').extract()
        # page = urllib.request.urlopen(self.start_urls[0]).read().decode("utf-8")
        # pat = '<img src="(.*?)"'
        # res = re.compile(pat,re.S).findall(page)
        # # print("getting data...")
        # print(res)
        # print(next_url)
        # print(response.body)
        pass