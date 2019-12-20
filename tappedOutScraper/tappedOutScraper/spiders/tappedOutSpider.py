# -*- coding: utf-8 -*-
import scrapy


class TappedoutspiderSpider(scrapy.Spider):
    name = 'tappedOutSpider'
    allowed_domains = ['amazon.com']
    start_urls = ['http://amazon.com/']

    def parse(self, response):
        pass
