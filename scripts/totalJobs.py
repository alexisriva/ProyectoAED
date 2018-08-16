# coding=utf-8

from scrapy.spiders import CrawlSpider
from scrapy.item import Item, Field


class totalItem(Item):
    city = Field()
    job_offer = Field()
    total_offers = Field()


class totalSpider(CrawlSpider):
    name = "totalSpider"
    allowed_domains=['www.indeed.co.uk']
    start_urls=['https://www.indeed.co.uk/jobs?q=big+data&l=london']

    def parse(self, response):
        search_count = response.xpath('//div[@id="searchCount"]/text()').extract_first().strip()
        item = totalItem()
        item['city'] = 'London'
        item['job_offer'] = 'Big Data'
        item['total_offers'] = search_count.split(" ")[-1]
        yield item
