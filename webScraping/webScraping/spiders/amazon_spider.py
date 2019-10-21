#to initialize project from top directory:
#scrapy genspider spider_name websiteToScrape.com

#returns title, author, price, and cover image
	#of books released in the last 30 days on amazon

# -*- coding: utf-8 -*-
import scrapy
# . is current directory
# .._ is equivilant to  saying 'get file _ from the directory above'
# ../_ 'go to the directory above, then navigate to directory _'
from ..items import AmazonTutorialItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = ['https://www.amazon.com/Books-Last-30-days/s?rh=n%3A283155%2Cp_n_publication_date%3A1250226011']
    # start_urls = ['http://amazon.com/']

    def parse(self, response):
    	#items stores instance of AmazonTutorialItem class
    	items = AmazonTutorialItem()

    	#add ::text so that only text of the tag gets extracted. NOT the tag itself
    	product_name = response.css('.a-color-base.a-text-normal').css('::text').extract()
    	product_author = response.css('.a-color-secondary .a-size-base.a-link-normal').css('::text').extract()
    	product_price = response.css('.a-spacing-top-small .a-price span span').css('::text').extract()
    	#does not extract image, extracts element that CONTAINS the image
    	product_cover_image_link = response.css('.s-image::attr(src)').extract()

    	items['book_title'] = product_name
    	items['book_author'] = product_author
    	items['book_price'] = product_price
    	items['cover_image'] = product_cover_image_link

    	yield items
