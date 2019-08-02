import scrapy
from maitian.items import MaitianItem

class MaitianSpider(scrapy.Spider):
    name = "zufang"
    start_urls = ['http://bj.maitian.cn/zfall/PG1']
    def parse(self, response):
        for zufang_itme in response.xpath('//div[@class="list_title"]'):
            yield {
                'title': zufang_itme.xpath('./h1/a/text()').extract_first().strip(),
                'price': zufang_itme.xpath('./div[@class="the_price"]/ol/strong/span/text()').extract_first().strip(),
                'area': zufang_itme.xpath('./p/span/text()').extract_first().replace('㎡','')
.strip(),
                'district': zufang_itme.xpath('./p//text()').re(r'昌平|朝阳|东城|大兴|丰台|海淀|石景山|顺义|通州|西城')[0],
            }

        next_page_url = response.xpath('//div[@id="paging"]/a[@class="down_page"]/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
