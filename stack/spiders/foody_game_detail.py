from scrapy import Spider
from scrapy.selector import Selector

from stack.items import BaseDetailItem
from stack.spiders.cinema_spider import CinemaSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from stack.spiders.cinema_spider import CinemaSpider

class FoodyGameDetailSpider(Spider): 

    name = "foody_game_detail"
    allowed_domains = ["http://foody.vn/"]
    
    f = open("foody_game_detail_url.txt")
    start_urls = [url.strip() for url in f.readlines()]
    del start_urls[-1]
    f.close()
    	
    def parse(self, response):
       itemSelects = Selector(response).xpath('/html/body/div[3]')

       for itemSelect in itemSelects:
            item = BaseDetailItem()

            item['name'] = itemSelect.xpath(
                'section[1]/div/div/div/div[1]/div/div[4]/div[3]/div/div[1]/div[2]/h1/text()').extract()[0]
            try:
                item['organizer_phone'] = itemSelect.xpath(
                'div[1]/p[last()]/text()[2]').extract()[0]        
            except:
                item['organizer_phone'] = "Unkown-parse error"

            try:
                item['address'] = itemSelect.xpath(
                'section[1]/div/div/div/div[1]/div/div[4]/div[3]/div/div[1]/div[4]/div[1]/div/div/span[2]/a/text()').extract()[0]      
            except:
                item['address'] = "Unkown-parse error"
       
            item['event_information'] = itemSelect.xpath(
                '/html/head/meta[9]/@content').extract()[0]

            item['lat'] = itemSelect.xpath(
                '/html/head/meta[14]/@content').extract()[0]
            item['lng'] = itemSelect.xpath(
                '/html/head/meta[15]/@content').extract()[0]
           
            #print item
            yield item

