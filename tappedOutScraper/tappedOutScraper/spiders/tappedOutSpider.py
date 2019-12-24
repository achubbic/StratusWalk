# -*- coding: utf-8 -*-

#to run:
#cd into tappedOutScaper directory and run
#scrapy crawl tappedOutSpider -o spiderOutput.json -a url=https://tappedout.net/mtg-decks/05-12-19-muldrotha-40/
import scrapy
import sys
from ..items import TappedoutscraperItem

class TappedoutspiderSpider(scrapy.Spider):
	name = 'tappedOutSpider'
	# start_urls = ['https://tappedout.net/mtg-decks/05-12-19-muldrotha-40/']

	def start_requests(self):
		yield scrapy.Request('%s' % self.url)

	def parse(self, response):
		#parenthesis indicate it is a class object
		items = TappedoutscraperItem()
		my_name = response.css('.card-hover::text').extract()
		items['card_name'] = my_name
		yield items
