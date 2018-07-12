# coding=utf-8

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field


class jobItem(Item):
    job = Field()
    company = Field()
    number_of_evaluations = Field()
    summary = Field()


class jobSpider(CrawlSpider):
    name = "jobSpider"
    allowed_domains=['co.indeed.com']
    start_urls=['https://co.indeed.com/jobs?q=big+data&l=Bogot%C3%A1%2C+Distrito+Capital%2C+Cundinamarca']

    rules = (Rule(
            LinkExtractor(allow=(), restrict_xpaths=('//a[span="Siguiente\xa0&raquo"]',)),
            callback="parse_page",
            follow=True
        ),
    )

    def parse_page(self, response):
        result = response.css('div[id^=p_].row.result')

        for i in range(len(result)):
            item = jobItem()

            item['job'] = result[i].css('h2.jobtitle a::attr(title)').extract_first()

            if result[i].css('span.company a::text').extract():
                item['company'] = result[i].css('span.company a::text').extract_first().strip()
            elif result[i].css('span.company::text').extract():
                item['company'] = result[i].css('span.company::text').extract_first().strip()
                item['number_of_evaluations'] =  "-"
            else:
                item['company'] = "-"
                item['number_of_evaluations'] = "-"

            if result[i].css('a span.slNoUnderline::text').extract():
                item['number_of_evaluations'] = result[i].css('a span.slNoUnderline::text').extract_first()

            item['summary'] = result[i].xpath('normalize-space(//span[@class="summary"])').extract_first()

            yield item