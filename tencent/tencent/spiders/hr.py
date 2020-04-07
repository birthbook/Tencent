# -*- coding: utf-8 -*-
import scrapy
from tencent.items import HrItem

class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?keywords=python&lid=2156']

    def parse_url(self, response):
        detail_urls = response.css('tr.even a::attr(href),tr.odd a::attr(href)').extract()
        for url in detail_urls:
            fullurl = response.urljoin(url)
            yield scrapy.Request(url=fullurl,callback=self.parse,meta={
                 'dont_redirect': True,
                 'handle_httpstatus_list': [302]
                },)

        #获取下一页的url地址
        next_url = response.css("#next::attr(href)").extract_first()
        if next_url != "javascript:;":
            url = response.urljoin(next_url)
            yield scrapy.Request(url=url,callback=self.parse,meta={
                 'dont_redirect': True,
                 'handle_httpstatus_list': [302]
                },)


    # 解析详情页
    def parse(self,response):
        item = HrItem()
        item["id"] = response.selector.re_first('onclick="applyPosition\(([0-9]+)\);"')
        item["title"] = response.css('#sharetitle::text').extract_first()
        item["location"] = response.selector.re_first('<span class="lightblue l2">工作地点：</span>(.*?)</td>')
        item["type"] = response.selector.re_first('<span class="lightblue">职位类别：</span>(.*?)</td>')
        item["number"] = response.selector.re_first('<span class="lightblue">招聘人数：</span>([0-9]+)人</td>')
        duty = response.xpath('//table//tr[3]//li/text()').extract()
        item["duty"] = ''.join(duty)
        requirement = response.xpath('//table//tr[4]//li/text()').extract()
        item["requirement"] = ''.join(requirement)
        yield item
