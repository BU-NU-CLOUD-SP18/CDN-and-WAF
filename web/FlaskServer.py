import flask
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db
from models import User

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:cloud528@128.31.25.73/FlaskServer"

db.init_app(application)
migrate = Migrate(application, db)

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
    users = User.query.all()
    return render_template('guest_list.html', guests=users)

@application.route('/register', methods = ['GET'])
def view_registration_form():
    return render_template('guest_registration.html')

@application.route('/register', methods = ['POST'])
def register_guest():
    name = request.form.get('name')
    email = request.form.get('email')


    user = User(name, email)
    db.session.add(user)
    db.session.commit()

    return render_template('guest_confirmation.html',
        name=name, email=email)

@application.route("/signup")
def signup():
    return render_template('register.html')

@application.route("/instances")
def instances():
    return render_template('instances.html')

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

# Save e-mail to database and send to success page
@application.route('/prereg', methods=['POST'])
def prereg():
    email = None
    if request.method == 'POST':
        email = request.form['email']
        # Check that email does not already exist (not a great query, but works)
        if not db.session.query(User).filter(User.email == email).count():
            reg = User(email)
            db.session.add(reg)
            db.session.commit()
            return render_template('success.html')
    return render_template('index.html')


if __name__ == "__main__":
    application.config['SECRET_KEY'] = "CDN-with_WAF"
    application.run(host='0.0.0.0', debug=True, port=6081)