# coding=utf-8

from scrapy.spiders import CrawlSpider
from scrapy.item import Item, Field

cities = ['New York, NY', 'San Francisco, CA']
jobs = ['Big Data', 'Data Science', 'Machine Learning']

def urlSplit(url):
    data = []
    for w in url.split('?')[-1].split('&'):
        data.append(w.split('=')[-1].replace("%20", " "))
    return data

def strNumberToInt(num):
    numl = num.split(',')
    return ''.join(numl)

class DiceItem(Item):
    city = Field()
    job_offer = Field()
    total_offers = Field()


class DiceSpider(CrawlSpider):
    name = "DiceSpider"
    allowed_domains = ['www.dice.com']
    start_urls = ['https://www.dice.com/jobs?q={}&l={}'.format(job, city) for job in jobs for city in cities]

    def parse(self, response):
        data = urlSplit(response.request.url)
        print(response.request.url)
        search_count = response.xpath('//span[@id="posiCountId"]/text()').extract_first().strip()
        print(search_count)
        item = DiceItem()
        item['city'] = data[1].split(',')[0]
        item['job_offer'] = data[0]
        item['total_offers'] = strNumberToInt(search_count)
        yield item
