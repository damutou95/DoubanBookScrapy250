import scrapy
from scrapy.loader import ItemLoader
from Douban250.items import Douban250Item
from scrapy.spiders.crawl import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor
class BookSpider(CrawlSpider):
    name = 'book'
    start_urls = ['https://book.douban.com/top250?icn=index-book250-all']
    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[@class = "pl2"]/a'),callback = 'parse_item'),
        Rule(LinkExtractor(restrict_xpaths='//span[@class = "next"]/a'),follow=True),
        )
    def parse_item(self,response):
        I = ItemLoader(item=Douban250Item(),response=response)
        I.add_xpath('BookName','//h1/span/text()')
        I.add_xpath('Author','//div[@id="info"]/span[contains(text(),"作者:")]/following-sibling::a[1]/text()')
        I.add_xpath('Press','//div[@id="info"]/span[contains(text(),"出版社:")]/following::text()[1]')
        I.add_xpath('Time','//div[@id="info"]/span[contains(text(),"出版年:")]/following::text()[1]')
        I.add_xpath('Price','//div[@id="info"]/span[contains(text(),"定价:")]/following::text()[1]')
        I.add_xpath('Score','//*[contains(@class,"rating_num")]/text()')
        return I.load_item()





