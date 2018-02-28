# models.py
import flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

# database model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))

    def __init__(self, email):
        self.email = email

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
        return '<varnishIp %r, >' % self.varnishIp
