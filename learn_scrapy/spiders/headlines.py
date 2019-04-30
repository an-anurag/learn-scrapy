# -*- coding: utf-8 -*-
import scrapy


class HeadlinesSpider(scrapy.Spider):
    name = 'headlines'
    allowed_domains = ['nytimes.com']
    start_urls = ['http://nytimes.com/']

    def parse(self, response):
        heads = response.xpath('//*[@class="collection"]/article/h2/a/')

        for h in heads:
            top = response.xpath('//*[@class="collection"]/article/h2/a/text()').extract_first()

