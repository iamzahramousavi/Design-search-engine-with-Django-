from tasnim_crawler.spiders.Tasnim import TasnimSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(TasnimSpider)
    process.start()

if __name__ == '__main__':
    main()