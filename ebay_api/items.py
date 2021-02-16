# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EbayApiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Title = scrappy.Field()
    Sold_Date = scrappy.Field()
    Sold_Price = scrappy.Field()
    Bids = scrappy.Field()
    Card_Link = scrappy.Field()
    Image_Link = scrappy.Field()
    pass
