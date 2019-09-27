# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class DangdangSpiderPipeline(object):
    def process_item(self, item, spider):
        con = pymysql.connect(host="127.0.0.1",user="root",passwd="root",db="dd")
        # cur = con.cursor()
        for i in range(0,len(item["link"])):
            title = item["title"][i]
            link = item["link"][i]
            comment = item["comment"][i]
            # print(title+";"+link+";"+comment)
            sql = "INSERT INTO goods(title,link,comment)value ('"+title+"','"+link+"','"+comment+"');"
            # print(sql)
            try:
                con.query(sql)
                print("正在写入第" + str(i) + "条数据")
                # cur.execute(sql)
                con.commit()
            except Exception as e:
                print(e)
            # cur.execute(sql)
            # con.commit()
        con.close()
        return item
