# -*- coding: utf-8 -*-
import scrapy


class ErshoufangSpider(scrapy.Spider):
    name = 'ershoufang'
    allowed_domains = ['maitian.com']
    start_urls = ['http://maitian.com/']

    def parse(self, response):
        pass
