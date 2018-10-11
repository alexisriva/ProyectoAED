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

class IndeedItem(Item):
    city = Field()
    job_offer = Field()
    total_offers = Field()


class IndeedSpider(CrawlSpider):
    name = "IndeedSpider"
    allowed_domains = ['www.indeed.com']
    start_urls = ['https://www.indeed.com/jobs?q={}&l={}'.format(job, city) for job in jobs for city in cities]

    def parse(self, response):
        data = urlSplit(response.request.url)
        search_count = response.xpath('//div[@id="searchCount"]/text()').extract_first().strip()
        item = IndeedItem()
        item['city'] = data[1].split(',')[0]
        item['job_offer'] = data[0]
        item['total_offers'] = strNumberToInt(search_count.split(" ")[-2])
        yield item
