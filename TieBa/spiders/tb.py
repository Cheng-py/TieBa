# -*- coding: utf-8 -*-
import scrapy
from ..items import TiebaItem

class TbSpider(scrapy.Spider):
    name = 'tb'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/f?ie=utf-8&kw=DNF&fr=search']

    def parse(self, response):
        items = TiebaItem()
        items["Title"] = response.xpath('.//div[contains(@class,"threadlist_title pull_left j_th_tit ")]/a/@title').extract()
        items["Author"] = response.xpath('.//div[contains(@class,"threadlist_author pull_right")]//span[contains(@class,"frs-author-name-wrap")]/a/text()').extract()
        print(items["Title"])
        print(len(items["Title"]))
        yield items
