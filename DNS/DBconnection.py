from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, scoped_session
from models import *

engine = create_engine('postgresql://ubuntu:528@10.0.0.9/cdn')
# engine = create_engine('postgresql://ubuntu:528@128.31.25.73/')

# Session = sessionmaker(bind=engine)
# session = scoped_session(sessionmaker(bind=engine))
# for instance in session.query(Users.email).all():
#     print(instance)
# =======
# import flask
# from flask import Flask, render_template, request, redirect, url_for, flash
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import scoped_session, sessionmaker, Query
#
# from models import *
print("comes here")
db_session = scoped_session(sessionmaker(bind=engine))
print("comes here 2")
Users = db_session.query(Users).all()
print("comes here 3")
for User in Users:
    print(User.email)
#print(Users.email)

# print(session.query('users'))
