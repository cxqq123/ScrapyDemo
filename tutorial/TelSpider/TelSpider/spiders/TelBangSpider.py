# -*- coding: utf-8 -*-
import scrapy
from ..items import TelspiderItem
class TelBangSpider(scrapy.Spider):
    name = "TelBangSpider"
    allowed_domains = ["www.dianhua.cn"]
    start_urls = ['http://www.dianhua.cn/beijing/c201/']


    def parse(self, response):
        mingyan = response.css("div.c_right_list")
        item = TelspiderItem()
        for v in mingyan:
            # item['content'] = v.css('.text::text').extract_first()  # 提取名言
            # tags = v.css('.tags .tag::text').extract()  # 提取标签
            # li.next a::attr(href)
            item['companyName'] = v.css('h5 a::text').extract_first()
            item['companyPhone'] = v.css('.tel_list p::text').extract_first()
            item['phoneType'] = v.css('.tel_list p span::text').extract_first()
            item['companyIcon'] = v.css('dd img::attr(src)').extract_first()
            item['companyDetailArea'] = v.css('._c_addr::text').extract_first()
            item['companyArea'] = ''
            # item['companyArea'] = v.css('.right p:e1(1)::text').extract_first()

            # item['companyPhone'] = v.css('.tel_list p :: text').extract_first()
            # item['phoneType'] = v.css('.tel_list p span :: text').extract_first()
            # item['companyIcon'] = v.css('dd img :: src').extract_first()
            # item['companyDetailArea'] = v.css('._c_addr :: text').extract_first()
            # item['companyArea'] = v.css('.right p:e1(1) :: text').extract_first()
            yield item  # 把取到的数据提交给pipline处理

        start_url = 'http://www.dianhua.cn'
        next_page = response.css('.page_box a::attr(href)').extract()[10]  # css选择器提取下一页链接
        next_page = start_url + next_page;
        print("next_page", next_page)
        if next_page is not None:  # 判断是否存在下一页
            next_page = response.urljoin(next_page)
            print("next_page 22", next_page)
            yield scrapy.Request(next_page, callback=self.parse)  # 提交给parse继续抓取下一页
