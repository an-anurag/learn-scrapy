# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
import time
from selenium.common.exceptions import NoSuchElementException


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com/']

    def start_requests(self):
        self.driver = webdriver.Chrome(executable_path='/media/capricorn/Origin_13/Master/Apps/DevWorx/Testing/chromedriver_linux64/chromedriver')
        self.driver.get("http://books.toscrape.com//")

        while True:
            try:
                next_page = self.driver.find_element_by_xpath('//a[text()="next"]')
                time.sleep(3)
                self.logger.info('Sleeping for 3 seconds')
                next_page.click()
                sel = Selector(text=self.driver.page_source)
                book_names = sel.xpath('//h3/a/text()').extract()
                print(book_names)

            except NoSuchElementException:
                self.logger.info("No next page to load")
                self.driver.quit()
                break