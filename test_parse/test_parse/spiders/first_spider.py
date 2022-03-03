import scrapy


class FirstSpider(scrapy.Spider):
    name = 'oz_spider'
    start_urls = ['https://oz.by/books/topic1602.html']

    def parse(self, response):
        for link in response.css('div.item-type-card__inner a::attr(href)'):
            yield response.follow(link, callback=self.parse_book)

        for i in range(1, 30):
            next_page = f'https://oz.by/books/topic1602.html?page={i}/'
            yield response.follow(next_page, callback=self.parse)

    def parse_book(self, response):
        yield{
            'title': response.css('div.b-product-title__heading h1::text').get(),
            'author': response.css('div.b-product-title__author a::text').get(),
            'year': response.css('div.b-product-title__author').get().split()[-2],
            'price':  " ".join(response.css('div.b-product-control__row span::text').get().split())
        }
