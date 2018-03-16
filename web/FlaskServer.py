import flask
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import hashlib, uuid

from models import *
from models import Users
#from models import db

application = Flask(__name__)

from sqlalchemy.orm import scoped_session, sessionmaker, Query
db_session = scoped_session(sessionmaker(bind=engine))
salt = uuid.uuid5(uuid.NAMESPACE_DNS, 'cdn').hex.encode('utf-8')

#backend function
def isUserInDB(email):
    if db_session.query(Users).filter(Users.email == email).all():
        return True
    else:
        return False

def isPasswdCorr(email, passwd):
    passwd_db = hashlib.sha512(passwd + salt).hexdigest()
    if db_session.query(Users).filter(Users.email == email).filter(Users.passwd == passwd_db).all():
        return True
    else:
        return False

@application.route("/index")
def index():
    return render_template('index.html')

# User List page
@application.route('/')
def view_registered_users():
    users = db_session.query(Users)
    return render_template('guest_list.html', Users=users)

@application.route("/signup", methods = ['GET'])
def view_signup():
    return render_template('register.html')

# Official Signup page
@application.route("/signup", methods = ['POST'])
def register_user():
    username = request.form.get('name')
    email = request.form.get('email')
    passwd_plaintext = request.form.get('password').encode('utf-8')
    passwd = hashlib.sha512(passwd_plaintext + salt).hexdigest()
    if isUserInDB(email):
        flash('email already exists!')
        return flask.redirect(flask.url_for('register_user'))
    user = Users(username, email, passwd)
    db_session.add(user)
    db_session.commit()
    return render_template('guest_confirmation.html',
        name=username, email=email)

# Instances status page
@application.route("/status")
def instances():
    instances = db_session.query(InstanceData)
    return render_template('status.html', instances = instances)

@application.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

@application.route('/login', methods=['POST'])
def login_user():
    try:
        email = request.form.get('email')
        passwd = request.form.get('passwd').encode('utf-8')
        if not isUserInDB(email):
            flash('user non-exist')
            return flask.redirect(flask.url_for('login_user'))
        if not isPasswdCorr(email, passwd):
            flash("password incorrect")
            return flask.redirect(flask.url_for('login_user'))
    except:
        flash("fields cannot be blank")
        return flask.redirect(flask.url_for('login_user'))
    return flask.redirect(flask.url_for('instances'))




if __name__ == "__main__":
    application.config['SECRET_KEY'] = "CDN-with_WAF"
    application.run(host='0.0.0.0', debug=True, port=6081)