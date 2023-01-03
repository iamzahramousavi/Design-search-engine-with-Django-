from mehr_crawler.spiders.Mehr import MehrNewsSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(MehrNewsSpider)
    process.start()

if __name__ == '__main__':
    main()