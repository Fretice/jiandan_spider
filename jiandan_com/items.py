# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class JiandanComItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class JiandanImsgItem(scrapy.Item):
    file_urls = Field()
    images = Field()
    file_paths = Field()
