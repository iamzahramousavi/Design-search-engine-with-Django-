from khabaronline_crawler.spiders.Khabaronline import KhabarOnlineSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(KhabarOnlineSpider)
    process.start()

if __name__ == '__main__':
    main()