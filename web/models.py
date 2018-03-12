# models.py
import flask
from flask_sqlalchemy import SQLAlchemy


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
        return '<varnishIp %r, >' % self.varnishIp


