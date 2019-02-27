# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TelspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    companyName = scrapy.Field()
    companyPhone = scrapy.Field()
    phoneType = scrapy.Field()
    companyIcon = scrapy.Field()
    companyDetailArea = scrapy.Field()
    companyArea = scrapy.Field()
    pass
