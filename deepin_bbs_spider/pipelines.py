# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DeepinBbsSpiderPipeline:
    def process_item(self, item, spider):
        print("获取每一条数据：")
        print(item)
        print(spider)
        return item
