import scrapy
from job_crawler.items import JobItem

class LinkedInSpider(scrapy.Spider):
    name = 'linkedin_spider'
    allowed_domains = ['linkedin.com']
    start_urls = ['https://www.linkedin.com/jobs/search/?keywords=your+keywords']

    def parse(self, response):
        # Extract job posting elements
        job_elements = response.xpath('//li[contains(@class, "job-card-container")]')

        for job in job_elements:
            item = JobItem()
            item['source'] = 'LinkedIn'  # Indicate the source of the job posting
            item['title'] = job.xpath('.//h3/text()').get()
            item['company'] = job.xpath('.//h4/a/text()').get()
            item['location'] = job.xpath('.//span[@class="job-result-card__location"]/text()').get()
            item['description'] = job.xpath('.//p[contains(@class, "job-result-card__snippet")]/text()').get()
            
            yield item