from scrapy import Spider
from scrapy.selector import Selector

from stack.items import StackItem
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from stack.spiders.cinema_spider import CinemaSpider

#process = CrawlerProcess(get_project_settings())
#process.crawl(CinemaSpider)
#process.start() # the script will block here until the crawling is finished