import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# https://by.wildberries.ru/catalog/


class SecondSpider(CrawlSpider):
    name = 'second_test_spider'
    start_urls = ['https://by.wildberries.ru/']

    rules = (
        Rule(LinkExtractor(allow='catalog'))
    )
