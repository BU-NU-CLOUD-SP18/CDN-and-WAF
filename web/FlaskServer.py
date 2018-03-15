import flask
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import *
from models import Users
#from models import db

application = Flask(__name__)

#application.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:cloud528@128.31.25.73/FlaskServer"

from sqlalchemy.orm import scoped_session, sessionmaker, Query
db_session = scoped_session(sessionmaker(bind=engine))

#db.init_app(application)
#migrate = Migrate(application, db)

#backend function
def isUserInDB(email):
    pass
def isPasswdCorr(email, passwd):
    pass

@application.route("/index")
def index():
    return render_template('index.html')

@application.route('/')
def view_registered_users():
    users = db_session.query(Users.email)
    return render_template('guest_list.html', guests=users)

@application.route('/register', methods = ['GET'])
def view_registration_form():
    return render_template('guest_registration.html')

@application.route('/register', methods = ['POST'])
def register_guest():
    username = request.form.get('name')
    email = request.form.get('email')
    passwd = request.form.get('password')

    user = Users(username, email, passwd)
    db_session.add(user)
    db_session.commit()

    return render_template('guest_confirmation.html',
        name=username, email=email)

@application.route("/signup", methods = ['GET'])
def view_signup():
    return render_template('register.html')

@application.route("/signup", methods = ['POST'])
def register_user():
    username = request.form.get('name')
    email = request.form.get('email')
    passwd = request.form.get('password')

    user = Users(username, email, passwd)
    db_session.add(user)
    db_session.commit()

    return render_template('guest_confirmation.html',
        name=username, email=email)

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
        passwd = request.form.get('passwd')
        if not isUserInDB(email):
            flash('user non-exist')
            return flask.redirect(flask.url_for('login_user'))
        if not isPasswdCorr(email, passwd):
            flash("password incorrect")
            return flask.redirect(flask.url_for('login_user'))
    except:
        flash("fields cannot be blank")
        return flask.redirect(flask.url_for('login_user'))
    return flask.redirect(flask.url_for('status'))




if __name__ == "__main__":
    application.config['SECRET_KEY'] = "CDN-with_WAF"
    application.run(host='0.0.0.0', debug=True, port=6081)