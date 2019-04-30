# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesSpiderItem(scrapy.Item):
    qoute = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()


class ImdbSpiderItem(scrapy.Item):
    image_urls = scrapy.Field()
    movie_name = scrapy.Field()
    release_year = scrapy.Field()
    director = scrapy.Field()
    images = scrapy.Field()
    image_name = scrapy.Field
