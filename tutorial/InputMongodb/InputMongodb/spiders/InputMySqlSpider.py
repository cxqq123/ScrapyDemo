# -*- coding: utf-8 -*-

import scrapy
from ..items import ScrapyMySqlItem

class InputMySqlSpider(scrapy.Spider):
    name = "inputMySqlSpider"
    allowed_domains = ["lab.scrapyd.cn"]
    start_urls = ['http://lab.scrapyd.cn/']

    def parse(self, response):
        mingyan = response.css("div.quote")
        item = ScrapyMySqlItem()

        for v in mingyan:
            item['content'] = v.css('.text::text').extract_first()  # 提取名言
            tags = v.css('.tags .tag::text').extract()  # 提取标签
            item['tag'] = ','.join(tags)  # 数组转换为字符串
            yield item  # 把取到的数据提交给pipline处理

        next_page = response.css('li.next a::attr(href)').extract_first()  # css选择器提取下一页链接
        if next_page is not None:  # 判断是否存在下一页
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)  # 提交给parse继续抓取下一页
