# import scrapy


# class QuotesSpider(scrapy.Spider):
#     name = "quotes"

#     def start_requests(self):
#         urls = [
#             'http://quotes.toscrape.com/page/1/',
#             'http://quotes.toscrape.com/page/2/',
#         ]
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)

#     def parse(self, response):
#         page = response.url.split("/")[-2]
#         filename = 'quotes-%s.html' % page
#         with open(filename, 'wb') as f:
#             f.write(response.body)
#         self.log('Saved file %s' % filename)

#schedules scrapy.Request objects returned by start_requests
#after receiving respinse, instantiates Response objects and passes said response as argument to Parse

#tldr: given url, creates primitive html file with text contents

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

#use scrapy quotes -o quotes.json to write results to a json file