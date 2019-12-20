# -*- coding: utf-8 -*-

#to run:
#cd into tappedOutScaper directory and run
#scrapy crawl tappedOutSpider -o spiderOutput.json
import scrapy
from ..items import TappedoutscraperItem

class TappedoutspiderSpider(scrapy.Spider):
	name = 'tappedOutSpider'
	start_urls = ['https://www.amazon.com/b?ie=UTF8&node=17276797011']

	def parse(self, response):
		#parenthesis indicate it is a class object
		items = TappedoutscraperItem()
		my_author = response.css('.s-access-title::text').extract()
		items['author_name'] = my_author
		yield items
