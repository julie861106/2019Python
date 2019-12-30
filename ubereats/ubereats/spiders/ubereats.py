FEED_EXPORT_ENCODING = 'utf-8'

import scrapy
#from ubereats.items import UbereatsItem

class UbercrawlSpider(scrapy.Spider):
    name = 'ubereats'

    # 可寫參數
    allowed_domains = ['https://www.ubereats.com/']

    # 爬蟲第一批request起始列表
    # yourURL = "https://www.ubereats.com/zh-TW/taipei/food-delivery/%E5%A3%AB%E6%9E%97%E7%B1%B3%E7%B2%89%E6%B9%AF/ULmFV4vjR7CIv1_wsvGA_A/?promo=5e0514e9-a9b5-443c-a5a9-1393b62640f9"
    yourURL = input("請輸入您要搜尋的URL位置>>>>>>")
    start_urls = [yourURL]

        
    def parse(self, response):


        for article in response.css('div.clamp-lines'):
            yield {
                'title': article.css("#clamped-content-menu_item_title::text").extract(),
                'price': article.css("div.b5.b6.c1.b8").extract_first()
                
            }
                