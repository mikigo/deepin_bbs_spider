import scrapy
from deepin_bbs_spider.items import DeepinBbsSpiderItem

class BbsSpiderSpider(scrapy.Spider):
    name = "bbs_spider"
    allowed_domains = ["bbs.deepin.org"]
    # start_urls = ["https://bbs.deepin.org/?offset=0&limit=20&order=updated_at&where=&languages=zh_CN#comment_title"]
    base_url = "https://bbs.deepin.org"


    def start_requests(self):
        for i in range(1):
            yield scrapy.Request(url=f"https://bbs.deepin.org/?offset={i}&limit=20&order=updated_at&where=&languages=zh_CN#comment_title")

    def parse(self, response):
        item = DeepinBbsSpiderItem()
        post_items = response.css("app-main-pc > div > div:nth-child(3) > app-post-pc")
        for post_item in post_items:
            item["url"] = post_item.css("a.post_lin_pc::attr(href)").get().replace("/en", self.base_url)
            item["title"] = "".join(post_item.css("span.ng-star-inserted::text").getall()[:2])
            # item["time"] = "".join(post_item.css("span.ng-star-inserted::text").getall()[3:])
            yield item

        # hrefs_list = response.css("div.myPage > app-pagination-v2 > a::attr(href)")
        # for href in hrefs_list:
        #     page_url = href.get().replace("/en", self.base_url)
        #     # print(page_url)
        #     yield scrapy.Request(url=page_url)


