# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from learn_scrapy.items import QuotesSpiderItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com//']

    def parse(self, response):
        l = ItemLoader(items=QuotesSpiderItem(), response=response)
        headline = response.xpath('//h1/a/text()').extract_first()

        container = response.xpath('//*[@class="quote"]')
        print(headline)
        for items in container:
            qoute = items.xpath('.//span/text()').extract_first()
            author = items.xpath('.//span[2]/small/text()').extract_first()
            tags = items.xpath('.//*[@itemprop="keywords"]/@content').extract_first()

            l.add_value('qoute', qoute)
            l.add_value('author', author)
            l.add_value('tags', tags)

            return l.load_item()

        # generating next page

        # next_page = response.xpath('//*[@class="next"]/a/@href').extract_first()
        # absolute_next_page = response.urljoin(next_page)
        # yield scrapy.Request(absolute_next_page, callback=self.parse)
