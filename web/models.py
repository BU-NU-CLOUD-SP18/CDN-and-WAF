# models.py
import flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://ubuntu:528@10.0.0.9/cdn')
# engine = create_engine('postgresql://ubuntu:528@128.31.25.73/cdn')
Base = declarative_base()
Base.metadata.reflect(engine)

from sqlalchemy.orm import relationship, backref



# database model from Postgres cdn. Table name 'UserData'
class Users(Base):
    __table__ = Base.metadata.tables['UserData']
    def __init__(self, username, email, passwd):
        self.username = username
        self.email = email
        self.passwd = passwd

class Instances(Base):
    __table__ = Base.metadata.tables['InstanceData']
    def __init__(self, cacheip, remark, cpu, storage):
        self.cacheip = cacheip
        self.remark = remark
        self.cpu = cpu
        self.storage = storage

class Joins(Base):
    __table__ = Base.metadata.tables['CacheMatch']
    def __init__(self, email, hostname, cacheset, origin_hostname):
        self.email = email
        self.hostname = hostname
        self.cacheset = cacheset
        self.origin_hostname = origin_hostname

class CNAME(Base):
    __table__ = Base.metadata.tables['CNAMEmatch']
    def __init__(self, cname, cacheip):
        self.cname = cname
        self.cacheip = cacheip
