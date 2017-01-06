# coding=UTF-8
from scrapy.spiders import Spider
from jiandan_com.items import JiandanImsgItem
from scrapy import Request


class download_jiandan(Spider):
    """docstring for download_jiandan."""
    name = 'download_jiandan'

    default_headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'www.jiandan.net',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    }

    start_urls = ['http://www.jiandan.net/ooxx/']

    def parse(self, response):
        list_imgs = response.css('a.view_img_link').xpath('@href').extract()
        if list_imgs:
            item = JiandanImsgItem()
            item['file_urls'] = list_imgs
            yield item

        next_page = response.css('div.comments div.cp-pagenavi a.previous-comment-page').xpath('@href').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield Request(next_page, callback=self.parse)
