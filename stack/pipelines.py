# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from sqlalchemy import create_engine, Table, Column, MetaData, Integer, Text
from scrapy.exceptions import DropItem
from sqlalchemy_utils import database_exists, create_database

class StackPipeline(object):

    def __init__(self):
        _engine = create_engine("postgresql:///data.db")
       
        if not database_exists(_engine.url):
    		create_database(_engine.url)

        _connection = _engine.connect()
        _metadata = MetaData()
        _stack_items = Table("questions", _metadata,
                             Column("id", Integer, primary_key=True),
                             Column("url", Text),
                             Column("title", Text))
        _metadata.create_all(_engine)
        self.connection = _connection
        self.stack_items = _stack_items

    def process_item(self, item, spider):
        is_valid = True
        for data in item:
            if not data:
                is_valid = False
                raise DropItem("Missing %s!" % data)
        if is_valid:
            ins_query = self.stack_items.insert().values(
                url=item["url"], title=item["title"])
            self.connection.execute(ins_query)
        return item
