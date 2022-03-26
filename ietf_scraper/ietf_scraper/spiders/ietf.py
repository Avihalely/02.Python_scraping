import scrapy
import w3lib.html


class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['https://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        return {
                'number':response.xpath('//span[@class="rfc-no"]/text()').get(),
                'title':response.xpath('//span[@class="title"]/text()').get(),

                'date':response.xpath('//span[@class="date"]/text()').get(),
                'author name ':response.xpath('//span[@class="author-name"]/text()').get(),
                'author company  ': response.xpath('//span[@class="author-company"]/text()').get(),
                'phone ': response.xpath('//span[@class="phone"]/text()').get(),
                'email ': response.xpath('//span[@class="email"]/text()').get(),
                'address ':response.xpath('//span[@class="address"]/text()').get(),

                'Description' : response.xpath('//meta[@name="DC.Description.Abstract"]/@content').get(),

                '**text ':w3lib.html.remove_tags(response.xpath('//div[@class="text"]/text()').get()),
                'sub-headings ':response.xpath('//meta[@class="subheading"]/text()').getall()
                }

