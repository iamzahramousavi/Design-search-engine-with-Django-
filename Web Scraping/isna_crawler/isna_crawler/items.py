# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IsnaCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # define the fields for your item here like:
    title = scrapy.Field()
    body = scrapy.Field()
    category = scrapy.Field()
    tags = scrapy.Field()
    pubDate = scrapy.Field()
    url = scrapy.Field()
