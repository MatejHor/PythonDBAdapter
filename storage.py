from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
import sqlalchemy

import sqlite3
import re

class Storage():
    DB_NAME = ''
    BASE = declarative_base()

    @classmethod
    def set_db(cls, database_name):
        cls.db_name = database_name

    @classmethod
    def create_db(cls, database_name):
        if database_name:
            Storage.set_db(f'sqlite:///{database_name}')
            sqlite3.connect(database_name)
            engine = create_engine(cls.db_name, echo=False, query_cache_size=0)
            cls.BASE.metadata.create_all(engine)
            return True
        
        print('[-] Database name was not defined')
        return False

    @classmethod
    def get_session(cls):
        engine = create_engine(cls.db_name, echo=False, query_cache_size=0)
        SESSION = sessionmaker()
        SESSION.configure(bind=engine)
        return SESSION
    
    @classmethod
    def get_connection(cls):
        return sqlite3.connect(re.sub('sqlite:///', '', cls.db_name))
    
    @classmethod
    def _get(cls, obj, filters, condition, output):
        condition = sqlalchemy.and_ if condition == 'and' else sqlalchemy.or_
        query_filters = [getattr(obj, key) == value for key, value in filters.items()]
        
        with Storage.get_session()() as session:
            query = session.query(obj).filter(condition(*query_filters))
            output = getattr(query, output)
            return output()
    
    @classmethod
    def get_list(cls, obj, filters, condition='and'):
        return cls._get(obj, filters, condition, 'all')
    
    @classmethod
    def get(cls, obj, filters, condition='and'):
        return cls._get(obj, filters, condition, 'first')

    @classmethod
    def add(cls, item):
        with Storage.get_session()() as session:
            session.add(item)
            session.commit()

    @classmethod
    def update(cls, old_item, new_item):
        del new_item.__dict__['_sa_instance_state']
        for key, value in new_item.items():
            field = getattr(old_item, key)
            if field != value:
                setattr(old_item, key, value)
        Storage.add(old_item)

    @classmethod
    def delete(cls, item):
        with Storage.get_session()() as session:
            session.delete(item)
            session.commit()
