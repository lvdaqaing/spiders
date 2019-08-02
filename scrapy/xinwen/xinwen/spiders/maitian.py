# -*- coding: utf-8 -*-
import scrapy


class MaitianSpider(scrapy.Spider):
    name = 'maitian'
    allowed_domains = ['maitian.com']
    start_urls = ['http://maitian.com/']

    def parse(self, response):
        pass
