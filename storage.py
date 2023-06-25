from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
import sqlalchemy

import sqlite3
import os

BASE = declarative_base()

class Storage():
    @staticmethod
    def set_db(database_name):
        os.environ['DB_NAME'] = database_name

    @staticmethod
    def create_db(database_name):
        if database_name:
            Storage.set_db(f'sqlite:///{database_name}')
            sqlite3.connect(database_name)
            engine = create_engine(os.getenv('DB_NAME'), echo=False, query_cache_size=0)
            BASE.metadata.create_all(engine)
            return True
        
        print('[-] Database name was not defined')
        return False

    @staticmethod
    def get_session():
        engine = create_engine(os.getenv('DB_NAME'), echo=False, query_cache_size=0)
        SESSION = sessionmaker()
        SESSION.configure(bind=engine)
        return SESSION

    @staticmethod
    def get_list(obj, filters, condition='and'):
        condition = sqlalchemy.and_ if condition == 'and' else sqlalchemy.or_
        query_filters = [getattr(obj, key) == value for key, value in filters.items()]
        with Storage.get_session()() as session:
            return session.query(obj).filter(condition(*query_filters)).all()
    
    @staticmethod
    def get(obj, key, value):
        column = getattr(obj, key)
        with Storage.get_session()() as session:
            return session.query(obj).filter(column == value).first()
    
    @staticmethod
    def add(item):
        with Storage.get_session()() as session:
            session.add(item)
            session.commit()

    @staticmethod
    def update(old_item, new_item):
        del new_item.__dict__['_sa_instance_state']
        for key, value in new_item.items():
            field = getattr(old_item, key)
            if field != value:
                setattr(old_item, key, value)
        Storage.add(old_item)

    @staticmethod
    def delete(item):
        with Storage.get_session()() as session:
            session.delete(item)
            session.commit()
