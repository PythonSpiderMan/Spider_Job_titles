# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
from __future__ import print_function
from scrapy import signals
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import logging


class JSMiddleware(object):
    def process_request(self, request, spider):
        # Headless
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        # spider initialization
        try: 
            spider.driver = webdriver.Remote(command_executor=spider.settings.get("SELENIUM_GRID_HUB_ADDR"), desired_capabilities=DesiredCapabilities.FIREFOX)
            spider.driver.get(request.url)
            body = spider.driver.page_source
            return HtmlResponse(spider.driver.current_url, body=body, encoding='utf-8', request=request)
        except: 
            logging.error("Remote Firefox Webdriver failed")

        try: 
            spider.driver = webdriver.Remote(command_executor=spider.settings.get("SELENIUM_GRID_HUB_ADDR"), desired_capabilities=DesiredCapabilities.CHROME)
            spider.driver.get(request.url)
            body = spider.driver.page_source
            return HtmlResponse(spider.driver.current_url, body=body, encoding='utf-8', request=request)
        except: 
            logging.error("Remote Chrome Webdriver failed")

        raise Exception("There is no webdriver available for me")

        # try:
        #     spider.driver = webdriver.Chrome(executable_path=os.path.join(os.getcwd(), 'chromedriver.exe'), chrome_options=chrome_options)
        #     spider.driver.get(request.url)
        #     body = spider.driver.page_source
        #     return HtmlResponse(spider.driver.current_url, body=body, encoding='utf-8', request=request)
        # except: 
        #     pass

        # try: 
        #     spider.driver = webdriver.Firefox(executable_path=os.path.join((os.getcwd(), 'geckodriver.exe')))
        #     spider.driver.get(request.url)
        #     body = spider.driver.page_source
        #     return HtmlResponse(spider.driver.current_url, body=body, encoding='utf-8', request=request)
        # except:
        #     raise Exception("There is no webdriver available for me")

       
class MonsterCategorySpiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
