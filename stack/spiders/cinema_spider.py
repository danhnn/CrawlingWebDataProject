from scrapy import Spider
from scrapy.selector import Selector

from stack.items import BaseUrlItem

class CinemaSpider(Spider):
    name = "cinema"
    allowed_domains = ["123phim.vn"]
    start_urls = [
        "http://www.123phim.vn",
    ]
 	
    def __init__(self):
        self.output_cinema_detail_url = []    # creates a new empty list for each dog

    def writeUrlToFile(self):
       print self.output_cinema_detail_url
       with open('cinema_detail_url.txt','a') as f:
        # write out the title and add a newline.
         f.truncate(0)
         for url in self.output_cinema_detail_url:
           f.write(url + "\n")
       return

    def parse(self, response):
       output_cinema_detail_url = []
       itemSelectors = Selector(response).xpath('//*[@id="menu-hide"]/div[3]/div[3]/div/div/ul/li/div')
       
       for itemSelector in itemSelectors:
            item = BaseUrlItem()
            item['title'] = itemSelector.xpath(
                'a/text()').extract()[0]
            item['url'] = itemSelector.xpath(
                'a/@href').extract()[0]
            self.output_cinema_detail_url.append(CinemaSpider.start_urls[0] + item['url']) 
            #yield item
       
       self.writeUrlToFile()
    
    