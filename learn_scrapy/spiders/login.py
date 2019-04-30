# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser


class NewsSpider(scrapy.Spider):
    name = 'news'
    start_urls = ['http://127.0.0.1:8000/staff/login',
                  'http://127.0.0.1:8000/students/student-list/']

    def parse(self, response):
        token = response.xpath('//form/input/@value').extract()
        return FormRequest.from_response(response, formdata={
            'csrfmiddlewaretoken': token,
            'username': 'an.anurag@msn.com',
            'password': 'Gpa$$i0n',
        }, callback=self.scrape_students)

    def scrape_students(self, response):
        open_in_browser(response)
        student_name = response.xpath('//tr/td/a/text()').extract()
        yield {'Student Name': student_name}

