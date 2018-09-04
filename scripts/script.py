# coding=utf-8

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field
from functions import normalize_whitespace


class jobItem(Item):
    job = Field()
    company = Field()
    summary = Field()


class jobSpider(CrawlSpider):
    name = "jobSpider"
    allowed_domains=['www.indeed.fr']
    start_urls=['https://www.indeed.fr/emplois?q=machine+learning&l=Paris']

    rules = (Rule(
            LinkExtractor(allow=(), restrict_xpaths=('//a[span="Suivant\xa0»"]',)), #Next\xa0&raquo»
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
            else:
                item['company'] = "-"

            item['summary'] = normalize_whitespace(' '.join(result[i].css('span.summary').extract_first().split()))

            yield item