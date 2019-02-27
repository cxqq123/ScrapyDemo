# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BendibaoItem(scrapy.Item):
    cname = scrapy.Field()
    ctime = scrapy.Field()
    address = scrapy.Field()
    price = scrapy.Field()
    photo = scrapy.Field()
    urlLink = scrapy.Field()
    pass
