import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from tasnim_crawler.items import TasnimCrawlerItem


class TasnimSpider(CrawlSpider):
    name = 'Tasnim'
    allowed_domains = ['www.tasnimnews.com']
    start_urls = []

    year_start = int(input('Give starting year: '))
    month_start = int(input('Give starting month: '))
    day_start = int(input('Give starting day: '))
    
    year_end = int(input('Give ending year: ')) 
    month_end = int(input('Give ending month: '))
    day_end = int(input('Give ending day: '))
    
    for yr in range(year_start, year_end + 1):
        for mn in range(month_start, month_end + 1):
            for dy in range(day_start, day_end + 1):
                url = f"https://www.tasnimnews.com/fa/archive/?date={yr}%2f{mn}%2f{dy}&sub=-1&service=-1&page=1"
                start_urls.append(url)


    rules = [Rule(LinkExtractor(allow=r'/fa/news/\d+/\d+/\d+/\d+/[^/]+$',), callback='parse_news', follow=False),
            Rule(LinkExtractor(allow=(r'/fa/archive/?\.*',)), follow=True)]

    def parse_news(self, response):
        self.logger.info(f"\n parse_news called\n{response.request.url}\n")
        item = TasnimCrawlerItem()
        item['url'] = response.request.url
        item['title'] = response.xpath('//h1[@class="title"]/text()').get().strip()
        item['body'] = ' '.join([x.strip() for x in (response.xpath('//div[@class="story"]/p//text()').getall())])
        item['category'] = response.xpath('//li[@class="service"]/a/text()').get()
        item['pubDate'] = response.xpath('//li[@class="time"]/text()').get()

        yield item
