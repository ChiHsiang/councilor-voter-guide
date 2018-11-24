# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
import os
import re
import json
import scrapy

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display


import common


class Spider(scrapy.Spider):
    name = "mayors"
    allowed_domains = ["www.cec.gov.tw"]
    start_urls = ["https://www.cec.gov.tw/pc/zh_TW/IDX/indexT.html",]
    download_delay = 1

    def __init__(self, ad=None, *args, **kwargs):
        super(Spider, self).__init__(*args, **kwargs)
        self.display = Display(visible=0, size=(800, 600))
        self.display.start()
        self.driver = webdriver.Chrome("/var/chromedriver/chromedriver")

    def spider_closed(self, spider):
        self.display.close()

    def parse(self, response):
        self.driver.get(response.url)
        nodes = scrapy.Selector(text=self.driver.page_source).xpath('//a[@target="_top"]')
        for node in nodes:
            constituency = int(re.search('\d', node.xpath('text()').extract_first()).group())
            yield response.follow(node, callback=self.parse_list, meta={'meta': constituency})

    def parse_list(self, response):
        for tr in response.css(u'table.tableT tr.trT'):
            d = {}
            d['type'] = 'councilors'
            d['county'] = response.xpath(u'//img[@alt="搜尋結果"]/following-sibling::b[1]/text()').extract_first().split()[0]
            d['constituency'] = response.meta['meta']
            d['elected'] = tr.xpath('td[1]/text()').extract_first().strip()
            d['number'] = int(tr.xpath('td[2]/text()').extract_first())
            d['votes'] = int(re.sub('\D', '', tr.xpath('td[5]/text()').extract_first()))
            d['votes_percentage'] = tr.xpath('td[6]/text()').extract_first()
            yield d
