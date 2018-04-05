import flask
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import scoped_session, sessionmaker, Query
import flask.ext.login as flask_login
import hashlib, uuid

from models import *
from models import Users
from models import Instances
from models import Joins

application = Flask(__name__)

login_manager = flask_login.LoginManager()
login_manager.init_app(application)

db_session = scoped_session(sessionmaker(bind=engine))
salt = uuid.uuid5(uuid.NAMESPACE_DNS, 'cdn').hex.encode('utf-8')

class User(flask_login.UserMixin):
    pass

@login_manager.user_loader
def user_loader(email):
    users = getUserList()
    if not (email) or email not in str(users):
        return
    user = User()
    user.id = email
    return user

def getUserList():
    return db_session.query(Users.email).all()


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

# User List page
@application.route('/')
def index():
    # the default should be the login page
    return render_template('login.html')

@application.route("/signup", methods = ['GET'])
def view_signup():
    return render_template('register.html')

# Official Signup page
@application.route("/signup", methods = ['POST'])
def register_user():
    username = request.form.get('name')
    email = request.form.get('email')
    passwd_again = request.form.get('password-again').encode('utf-8')
    passwd_plaintext = request.form.get('password').encode('utf-8')
    passwd = hashlib.sha512(passwd_plaintext + salt).hexdigest()
    if passwd_again != passwd_plaintext:
        flash('please type identical password!')
        return flask.redirect(flask.url_for('register_user'))
    if isUserInDB(email):
        flash('email already exists!')
        return flask.redirect(flask.url_for('register_user'))
    user = Users(username, email, passwd)
    db_session.add(user)
    db_session.commit()
    return render_template('guest_confirmation.html',
        name=username, email=email)

# Instances status page
@flask_login.login_required
@application.route("/status", methods=['GET', 'POST'])
def instances():
    uid = flask_login.current_user.id
    uname = db_session.query(Users.username).filter(Users.email == uid).all()[0]
    infos = db_session.query(Joins).filter(Joins.email == uid).all()
    for i in range(0, len(infos)):
        infos[i].CNAME = infos[i].hostname + '.foo.test.me'
    if request.method == 'POST':
        hostname = request.form.get('hostname')
        origin = request.form.get('origin-hostname')
        if hostname == "" or origin == "":
            flash("fields cannot be blank")
            return flask.redirect(flask.url_for('instances'))
        joins = Joins(uid, hostname, '9.9.9.9', origin)     # replace 9.9.9.9 into the real cacheip later
        db_session.add(joins)
        db_session.commit()
    return render_template('status.html', instances = infos, uname = uname)

@application.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

@application.route('/login', methods=['POST'])
def login_user():
    email = request.form.get('email')
    passwd = request.form.get('passwd').encode('utf-8')
    if not isUserInDB(email):
        flash('user non-exist')
        return flask.redirect(flask.url_for('login_user'))
    if not isPasswdCorr(email, passwd):
        flash("password incorrect")
        return flask.redirect(flask.url_for('login_user'))
    if not email or not passwd:
        flash("fields cannot be blank")
        return flask.redirect(flask.url_for('login_user'))
    user = User()
    user.id = email
    flask_login.login_user(user)
    return flask.redirect(flask.url_for('instances'))



if __name__ == "__main__":
    application.config['SECRET_KEY'] = "CDN-with_WAF"
    application.run(host='0.0.0.0', debug=True, port=6081)
    # application.run(host='0.0.0.0', debug=True, port=80)