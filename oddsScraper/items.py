# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem

from odds.models import odds


class FootballItem(scrapy.Item):
    # define the fields for your item here like:
	match = scrapy.Field()
	tournament = scrapy.Field()
	team1 = scrapy.Field()
	team2 = scrapy.Field()
	datetime = scrapy.Field()
	team1_odds = scrapy.Field()
	team2_odds = scrapy.Field()
	draw_odds = scrapy.Field()

class HorseracingItem(scrapy.Item):
	match = scrapy.Field()
	tournament = scrapy.Field()
	datetime = scrapy.Field()
	odds = scrapy.Field()

class GameItem(DjangoItem):
	django_model = odds
