# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MehrCrawlerItem(scrapy.Item):
    title = scrapy.Field()
    body = scrapy.Field()
    category = scrapy.Field()
    tags = scrapy.Field()
    pubDate = scrapy.Field()
    url = scrapy.Field()
