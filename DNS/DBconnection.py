import flask
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker, Query

from models import *

db_session = scoped_session(sessionmaker(bind=engine))
Users = db_session.query(Users.email).all()

for User in Users:
    print(User.email)


# print(session.query('users'))
