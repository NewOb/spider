# -*- coding: utf-8 -*-

# Scrapy settings for black project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'black'

SPIDER_MODULES = ['black.spiders']
NEWSPIDER_MODULE = 'black.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'black (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'black.middlewares.BlackSpiderMiddleware': 543,
# }
# IP池设置
PROXIES_NEW = {
  "http": [
    "http://61.135.217.7:80",
    "http://219.141.153.38:80",
    "http://583349285:2zectsyx@139.196.76.78:16816"
  ],
  "https": [
    "https://113.226.18.243:80",
    "https://121.31.100.209:8123",
    "https://14.117.177.135:808",
    "https://171.223.230.46:61234",
    "https://117.57.90.121:25435",
    "https://175.11.214.29:808",
    "https://118.190.145.138:9001",
    "https://182.112.89.23:8118",
    "https://221.228.17.172:8181",
    "https://115.46.70.48:8123",
    "https://110.88.30.36:808",
    "https://110.87.104.153:8118",
    "https://1.195.25.204:61234",
    "https://119.186.241.31:61234",
    "https://175.155.152.41:61234",
    "https://27.31.103.233:21973",
    "https://125.105.110.4:3128",
    "https://114.222.24.111:808",
    "https://140.250.180.229:61234",
    "https://120.83.98.216:61234",
    "https://175.155.223.179:61234",
    "https://115.198.37.56:6666",
    "https://115.46.74.192:8123",
    "https://106.56.102.39:8070",
    "https://125.121.121.155:6666",
    "https://219.157.147.113:8118",
    "https://117.66.167.57:8118",
    "https://183.128.242.93:6666",
    "https://115.198.39.24:6666",
    "https://114.223.162.171:8118",
    "https://115.46.89.82:8123",
    "https://58.208.16.70:37436",
    "https://123.188.6.176:1133",
    "https://112.195.51.225:61234",
    "https://112.193.131.17:8118",
    "https://221.234.250.204:8010",
    "https://49.79.67.119:61234",
    "https://220.184.215.223:6666",
    "https://180.121.134.176:808",
    "https://122.246.48.118:8010",
    "https://119.7.59.13:61234",
    "https://27.54.248.42:8000",
    "https://59.32.37.99:8010",
    "https://220.191.100.253:6666",
    "https://112.193.70.85:61234",
    "https://60.167.128.91:48963",
    "https://119.4.70.128:61234",
    "https://182.88.166.148:8123",
    "https://113.117.65.112:61234",
    "https://115.226.129.195:61234",
    "https://106.75.71.122:80",
    "https://125.122.171.167:6666",
    "https://125.118.144.247:6666",
    "https://60.184.173.221:8070",
    "https://60.190.250.120:8080",
    "https://36.6.146.199:47025",
    "https://106.56.102.78:808",
    "https://119.7.225.218:61234",
    "https://583349285:2zectsyx@139.196.76.78:16816"
  ]
}

# 用户代理（User-Agent）池设置
USER_AGENT_LIST = [
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
"Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5" ]

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#     'black.middlewares.BlackDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'black.pipelines.BlackPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
