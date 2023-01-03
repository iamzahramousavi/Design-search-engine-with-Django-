import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from fars_crawler.items import FarsCrawlerItem


class FarsSpider(CrawlSpider):
    name = 'Fars'
    allowed_domains = ['www.farsnews.ir']
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
                url = f"https://www.farsnews.ir/archive?cat=-1&subcat=-1&date={yr}%2F{mn}%2F{dy}&p=1"
                start_urls.append(url)

    rules = [Rule(LinkExtractor(allow=r'/news/\d+/[^/]+$',), callback='parse_news', follow=False),
             Rule(LinkExtractor(allow=(r'/archive\?\.*',)), follow=True)]

    def parse_news(self, response):
        self.logger.info(f"\n parse_news called\n{response.request.url}\n")
        item = FarsCrawlerItem()
        item['url'] = response.request.url
        item['title'] = response.xpath('//h1[@class="title mb-2 d-block text-justify"]/text()').get().strip()
        item['body'] = ' '.join([x.strip() for x in (response.xpath('//div[@class="nt-body text-right mt-4"]/p//text()').getall())])
        item['category'] = response.xpath('//h2[@class="category-name d-flex justify-content-center"]//a/text()').get().strip()
        item['pubDate'] = ''.join([x.strip() for x in (response.xpath('//div[@class="publish-time d-flex justify-content-center"]/time/text()').get())])
        item['tags'] = ' '.join([x.strip() for x in (response.xpath('//div[@class="tags mt-2 text-right d-flex flex-wrap"]//a/text()').getall())])

        yield item