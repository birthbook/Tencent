# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class TencentItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class HrItem(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    location = scrapy.Field()
    type = scrapy.Field()
    number = scrapy.Field()
    duty = scrapy.Field()
    requirement = scrapy.Field()