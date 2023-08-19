import scrapy

class JobItem(scrapy.Item):
    source = scrapy.Field()   # To indicate the source website
    title = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    description = scrapy.Field()