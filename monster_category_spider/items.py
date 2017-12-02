# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class MonsterCategorySpiderItem(scrapy.Item):
    full_category_name = Field()
    json_category_keys = Field()
