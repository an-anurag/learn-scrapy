# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.loader import ItemLoader
from learn_scrapy.items import ImdbSpiderItem


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    allowed_domains = ['imdb.com/']
    start_urls = ['https://imdb.com/chart/top?ref_=nv_mv_250/']

    def parse(self, response):
        movie_page_link = response.xpath('//tbody/tr/td[2]/a/@href').extract()
        for link in movie_page_link:
            absoulute_page_link = response.urljoin(link)
            yield Request(absoulute_page_link, dont_filter=True, callback=self.parse_movie)

    def parse_movie(self, response):
        l = ItemLoader(item=ImdbSpiderItem(), response=response)
        image_urls = response.xpath('//*[@class="poster"]/a/img/@src').extract_first()
        image_name = response.xpath('//*[@class="poster"]/a/img/@title').extract_first()
        movie_name = response.xpath('//*[@id="title-overview-widget"]/div[2]/div[2]/div/div[2]/div[2]/h1/text()').extract_first()
        release_year = response.xpath('//*[@id="title-overview-widget"]/div[2]/div[2]/div/div[2]/div[2]/h1/span/a/text()').extract_first()
        director = response.xpath('//*[@id="title-overview-widget"]/div[3]/div[1]/div[2]/span/a/span/text()').extract_first()

        print(image_urls)
        print(movie_name)
        print(release_year)
        print(director)

        # yield {
        #     'Poster': poster,
        #     'Movie Name': movie_name,
        #     'Release Year': release_year,
        #     'Director': director,
        # }

        l.add_value('image_urls', image_urls)
        l.add_value('movie_name', movie_name)
        l.add_value('release_year', release_year)
        l.add_value('director', director)
        l.add_value('image_name', image_name)

        return l.load_item()
