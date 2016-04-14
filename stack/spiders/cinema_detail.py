from scrapy import Spider
from scrapy.selector import Selector

from stack.items import CinemaDetailItem

class CinemaDetailSpider(Spider):
    name = "cinema_detail"
    allowed_domains = ["123phim.vn"]
    start_urls = [
        "http://www.123phim.vn/rap-chieu-phim/97-cinestar-quoc-thanh.html",
    ]
 	
    def parse(self, response):
       questions = Selector(response).xpath('//*[@id="menu-hide"]/div[3]/div[3]/div/div/ul/li/div')
       print "Leng quest = %d" % len(questions)

       for question in questions:
            item = StackItem()
            item['title'] = question.xpath(
                'a/text()').extract()[0]
            item['url'] = question.xpath(
                'a/@href').extract()[0]
            yield item