from scrapy import Spider
from scrapy.selector import Selector

from stack.items import CinemaDetailItem
from stack.spiders.cinema_spider import CinemaSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from stack.spiders.cinema_spider import CinemaSpider

class CinemaDetailSpider(Spider):
    name = "cinema_detail"
    allowed_domains = ["123phim.vn"]
    """
    start_urls = [
        "http://www.123phim.vn/rap-chieu-phim/97-cinestar-quoc-thanh.html",
        "http://www.123phim.vn/rap-chieu-phim/52-cgv-celadon-tan-phu.html"
    ]
    """
    
    f = open("cinema_detail_url.txt")
    start_urls = [url.strip() for url in f.readlines()]
    del start_urls[-1]
    f.close()
    
    def parse(self, response):
       #print CinemaDetailSpider.start_urls
       itemSelects = Selector(response).xpath('/html/body/section[2]/section/div[2]')

       for itemSelect in itemSelects:
            item = CinemaDetailItem()
            item['name'] = itemSelect.xpath(
                'div[1]/h3/text()').extract()[0]
            try:
                item['organizer_phone'] = itemSelect.xpath(
                'div[1]/p[last()]/text()[2]').extract()[0]        
            except:
                item['organizer_phone'] = "Unkown-parse error"

            try:
                item['address'] = itemSelect.xpath(
                'div[1]/p[last()]/text()[1]').extract()[0]      
            except:
                item['address'] = "Unkown-parse error"
       
            item['event_information'] = itemSelect.xpath(
                'div[1]/p[1]').extract()[0]
            item['lat'] = itemSelect.xpath(
                '//*[@id="cinema-map"]/@data-lat').extract()[0]
            item['lng'] = itemSelect.xpath(
                '//*[@id="cinema-map"]/@data-lng').extract()[0]
           
            #print item
            yield item