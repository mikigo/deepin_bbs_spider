from copy import deepcopy

import scrapy

from deepin_bbs_spider.items import DeepinBbsSpiderItem


class BbsSpiderSpider(scrapy.Spider):
    name = "bbs_spider"
    allowed_domains = ["bbs.deepin.org"]
    base_url = "https://bbs.deepin.org"

    def start_requests(self):
        for i in range(5):
            yield scrapy.Request(url=f"https://bbs.deepin.org/?offset={i}&limit=20&order=updated_at&where=&languages=zh_CN#comment_title")

    def parse(self, response):
        item = DeepinBbsSpiderItem()
        post_items = response.css("app-main-pc > div > div:nth-child(3) > app-post-pc")
        for post_item in post_items:
            item["url"] = post_item.css("a.post_lin_pc::attr(href)").get().replace("/en", self.base_url)
            item["title"] = "".join(post_item.css("span.ng-star-inserted::text").getall()[:2])
            yield scrapy.Request(
                url=item["url"],
                callback=self.post_parse,
                cb_kwargs={"item": deepcopy(item)}
            )

    def post_parse(self, response, **kwargs):
        item = kwargs["item"]
        post_info = "".join(
            response.css("div.post_conten > div.post_edit.ng-star-inserted > div > div > p::text").getall()
        )
        item["post_info"] = post_info
        yield deepcopy(item)
