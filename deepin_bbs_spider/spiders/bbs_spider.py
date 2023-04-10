import scrapy


class BbsSpiderSpider(scrapy.Spider):
    name = "bbs_spider"
    allowed_domains = ["bbs.deepin.org"]
    # start_urls = ["https://bbs.deepin.org/?offset=0&limit=20&order=updated_at&where=&languages=zh_CN#comment_title"]


    def start_requests(self):
        yield scrapy.Request(url="https://bbs.deepin.org/?offset=0&limit=20&order=updated_at&where=&languages=zh_CN#comment_title")

    def parse(self, response):
        post_items = response.css("app-main-pc > div > div:nth-child(3) > app-post-pc")
        for post_item in post_items:
            url = post_item.css("a.post_lin_pc::attr(href)").get()
            title = "".join( post_item.css("span.ng-star-inserted::text").getall()[:2])
            print(url, title)

