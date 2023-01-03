import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from isna_crawler.items import IsnaCrawlerItem


class IsnaSpider(CrawlSpider):
    name = 'Isna'
    allowed_domains = ['www.isna.ir']
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
                url = f"https://www.isna.ir/page/archive.xhtml?mn={mn}&wide=0&dy={dy}&ms=0&pi=1&yr={yr}"
                start_urls.append(url)

    rules = [Rule(LinkExtractor(allow=r'/news/\d+/[^/]+$',), callback='parse_news', follow=False),
             Rule(LinkExtractor(allow=(r'/page/archive.xhtml\?\.*',)), follow=True)]

    def parse_news(self, response):
        self.logger.info(f"\n parse_news called\n{response.request.url}\n")
        item = IsnaCrawlerItem()
        item['url'] = response.request.url
        item['title'] = response.xpath('//h1[@class="first-title"]/text()').get().strip()
        item['body'] = ' '.join([x.strip() for x in (response.xpath('//div[@class="item-text"]/p//text()')
                                                     .getall())])
        item['category'] = response.xpath('//span[@itemprop="articleSection"]/text()').get().strip()
        item['pubDate'] = response.xpath('//span[@class="text-meta"]/text()').get()
        item["tags"] = response.xpath('//footer[@class="tags"]//ul/li/a/text()').getall()

        yield item