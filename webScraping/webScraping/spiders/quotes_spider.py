import scrapy

class QuotesSpider(scrapy.Spider):
	name = "quotes" #identifies spider, unique

	def start_requests(self): #returns iterable Requests
								#indicates where spider begins crawl from
		urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
        	yield scrappy.Request(url=url, callback=self.parse)

    def parse(self, response): #
    	page = response.url.split("/")[-2]
    	filename = 'quotes-%s.html' % page
    	with open(filename, 'wb') as f:
    		f.write(response.body)
    	self.log('Saved file %s' % filename)