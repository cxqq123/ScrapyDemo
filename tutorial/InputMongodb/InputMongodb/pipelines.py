# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
class InputmongodbPipeline(object):

    def __init__(self):
        #连接mongo db 数据库
        client = pymongo.MongoClient('127.0.0.1', 27017)
        #新建一个数据库
        db = client['ScrapyChina']
        #新建一个表
        self.post = db['mingyan']

    def process_item(self, item, spider):
        #将对象转换成一个字典
        postItem = dict(item)
        #然后将该字典json 数据插入表中
        self.post.insert(postItem)
        return item
