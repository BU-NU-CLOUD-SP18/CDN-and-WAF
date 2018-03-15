# models.py
import flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://ubuntu:528@128.31.25.73/cdn')
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
        self.originip = None
"""
db = SQLAlchemy()

# database model
class User(db.Model):
    __tablename__ = "users"
    name = db.Column(db.String(120), primary_key=True, unique=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(120))
    originip = db.Column(db.String(120))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.originip = None

    def __repr__(self):
        return '<E-mail %r>' % self.email

class Instance(db.Model):
    __tablename__ = "instances"
    varnishIp = db.Column(db.Integer, primary_key=True)
    cpu = db.Column(db.String(120), unique=True)
    status = db.Column(db.String(120))

    def __init__(self, varnishIp, cpu, status):
        self.varnishIp = varnishIp
        self.cpu = cpu
        self.status = status

    def __repr__(self):
        return '<varnishIp %r, >' % self.varnishIp"""


