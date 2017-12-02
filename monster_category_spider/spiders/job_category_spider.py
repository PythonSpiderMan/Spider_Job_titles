# -*- coding: utf-8 -*-
import scrapy
from parsel import Selector
from ..items import MonsterCategorySpiderItem
import json


"""scrapy crawl job_category_spider -o job_titles.csv -t csv"""
class JobCategorySpiderSpider(scrapy.Spider):
    name = 'job_category_spider'
    allowed_domains = ['monster.com']
    start_urls = ['https://www.monster.com/jobs/job-title/A']

    def parse(self, response):
        for i in range(1, 27):
            xpath_job_letter = """//*[@id="jsr"]/div/div/div/div/div/ul[1]/li[%s]""" % str(i)
            self.driver.find_element_by_xpath(xpath_job_letter).click()

            xpath_job_title = """//*[@id="jsr"]/div/div/div/div/div/ul[2]/li/h3/a/text()"""
            job_titles = Selector(text=self.driver.page_source).xpath(xpath_job_title).extract()
            for job_title in job_titles:
                job_title = str(job_title).replace(" Jobs", "")
                category_keys = job_title.split()
                
                item = MonsterCategorySpiderItem()
                item['full_category_name'] = str(job_title)
                item['json_category_keys'] = json.dumps(category_keys)
                yield item

