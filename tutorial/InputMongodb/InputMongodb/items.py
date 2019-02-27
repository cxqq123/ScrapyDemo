# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class InputmongodbItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tag = scrapy.Field()
    cont = scrapy.Field()
    pass

class ScrapyMySqlItem(scrapy.Item):
    #标签字段
    tag = scrapy.Field()
    #名言内容
    content = scrapy.Field()
    pass