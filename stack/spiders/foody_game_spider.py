from scrapy import Spider
from scrapy.selector import Selector

from stack.items import BaseUrlItem

class FoodyGameSpider(Spider):
    name = "foody_game"
    allowed_domains = ["http://foody.vn/"]
    start_urls = [
        #"http://entertain.foody.vn/ho-chi-minh/khu-choi-game?page=5",
        #"http://entertain.foody.vn/ho-chi-minh/cong-vien-vui-choi?page=2",
        "http://shop.foody.vn/ho-chi-minh/trung-tam-thuong-mai?page=3",
        #"http://travel.foody.vn/ho-chi-minh/khu-du-lich?page=2",
    ]

    #detail_raw_url = "http://entertain.foody.vn"
    detail_raw_url = "http://shop.foody.vn"
	#detail_raw_url = "http://travel.foody.vn"

    def __init__(self):
        self.output_foody_game_detail_url = []    # creates a new empty list for each dog

    def writeUrlToFile(self):
       print self.output_foody_game_detail_url
       with open('foody_game_detail_url.txt','a') as f:

        # write out the title and add a newline.
         f.truncate(0)
         for url in self.output_foody_game_detail_url:
           f.write(url + "\n")
       return

    def parse(self, response):
  		#//*[@id="directorypage"]/div[2]/div/div/div/div[2]/div[5]/div[1]/div/div[4]/div[2]/div[1]/h2/a
       itemSelectors = Selector(response).xpath('//div[@class="result-name"]')
       print "ITEM Slector = %d" % len(itemSelectors)

       for itemSelector in itemSelectors:
            item = BaseUrlItem()
            item['title'] = itemSelector.xpath(
                'h2/a/text()').extract()[0]
            item['url'] = itemSelector.xpath(
                'h2/a/@href').extract()[0]
            self.output_foody_game_detail_url.append(FoodyGameSpider.detail_raw_url + item['url']) 
            #print item
           
       self.writeUrlToFile()
    
    