# -*- coding: utf-8 -*-
import scrapy
from ..items import BendibaoItem
class BenDiBaoSpider(scrapy.Spider):
    name = "BenDiBaoSpider"
    allowed_domains = ["ly.sz.bendibao.com"]
    start_urls = ['http://ly.sz.bendibao.com/tour/8972_2.html']


    def parse(self, response):
        play = response.css("div.section")
        item = BendibaoItem()
        for v in play:
            item['cname'] = v.css('dt a::text').extract_first()
            item['ctime'] = v.css('.icon_zise::text').extract()[0]
            item['address'] = v.css('.icon_zise::text').extract()[1]
            item['price'] = v.css('.icon_zise::text').extract()[2]
            item['photo'] = v.css('a img::attr(src)').extract_first()
            item['urlLink'] = v.css('dt a::attr(href)').extract_first()


            # item['photo'] = v.css('a img::attr(src)').extract_first()
            # item['urlLink'] = v.css('a:attr(href)').extract_first()
            yield item  # 把取到的数据提交给pipline处理

        start_url = 'http://ly.sz.bendibao.com'
        next_page = response.css('#ctl00_NextPage::attr(href)').extract_first()  # css选择器提取下一页链接
        print("next_page", next_page)
        if next_page is not None:  # 判断是否存在下一页
            next_page = response.urljoin(next_page)
            print("next_page 22", next_page)
            yield scrapy.Request(next_page, callback=self.parse)  # 提交给parse继续抓取下一页
