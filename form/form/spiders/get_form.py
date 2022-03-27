# -*- coding: utf-8 -*-
import scrapy


def generate_start_urls():
    names = ['Alice','Bob','Charles']
    quests = ['to seek the grail','to learn python','to scrape the web']
    return ['http://pythonscraping.com/linkedin/formAction.php?name={}&quest={}&color=blue'.format(name, quest) for name in names for quest in quests]

class GetFormSpider(scrapy.Spider):
    name = 'get_form'
    allowed_domains = ['https://pythonscraping.com/']
    start_urls = ['http://https://pythonscraping.com//']

    def parse(self, response):
        return {'text':response.xpath('//div[@class="wrapper"]/text()'.get())}
