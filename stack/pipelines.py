# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import datetime
from sqlalchemy import create_engine, Table, Column, MetaData, Integer, Text, Float, DateTime
from scrapy.exceptions import DropItem
from sqlalchemy_utils import database_exists, create_database

class CinemaPipeline(object):

    def __init__(self):
        _engine = create_engine("postgresql:///InterestingPlaceFiding_development")
       
        if not database_exists(_engine.url):
    		create_database(_engine.url)

        _connection = _engine.connect()
        _metadata = MetaData()
        
        _event_items = Table("events",_metadata, Column("id", Integer, primary_key=True),
                             Column("lat", Float),
                             Column("lng", Float),
                             Column("address", Float),
                             Column("event_information", Text),
                             Column("organizer_phone", Text),
                             Column("created_at", DateTime),
                             Column("updated_at", DateTime),
                             Column("name", Text))
                           
        self.event_items = _event_items
        
        _metadata.create_all(_engine)
        self.connection = _connection
      

    def process_item(self, item, spider):
        is_valid = True
        for data in item:
            if not data:
                is_valid = False
                raise DropItem("Missing %s!" % data)
        if is_valid:
            now = datetime.datetime.now()
            ins_query = self.event_items.insert().values(
                lat=item["lat"],lng=item["lng"], name=item["name"],
                organizer_phone=item["organizer_phone"],event_information=item["event_information"],
                address=item["address"],created_at=now,updated_at=now)
            self.connection.execute(ins_query)
        return item
