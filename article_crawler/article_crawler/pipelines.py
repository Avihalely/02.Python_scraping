# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# each tesks displays here as an class
# display all our data as an python object
from scrapy.exceptions import DropItem
from datetime import datetime


class CheckItemPipeline:
    def process_item(self, article, spider):
        if not article['lastUpdated'] or not article['url'] or not article['title']:
            raise DropItem('missing something')
        return article


class CleanDatePipline:
    def process_item(self, article, spider):
        article['lastUpdated'].replace('this page was last edited on ', '').strip()
        article['lastUpdated'] = datetime.strptime(article['lastUpdated'], '%d %B %Y, at %H%M')
        return article
