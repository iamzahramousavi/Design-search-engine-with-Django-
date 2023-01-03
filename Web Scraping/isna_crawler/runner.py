from isna_crawler.spiders.Isna import IsnaSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(IsnaSpider)
    process.start()

if __name__ == '__main__':
    main()