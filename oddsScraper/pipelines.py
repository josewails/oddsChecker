# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html



import psycopg2
import traceback
import json
import sys
from odds.models import odds

class OddscheckerPipeline(object):
    odds.objects.all().delete()
    def process_item(self, item, spider):
        item.save()
        return item
