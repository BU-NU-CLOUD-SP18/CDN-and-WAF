import flask
from flask import Flask, render_template, request, redirect, url_for, flash

application = Flask(__name__)

#backend function
def isUserInDB(email):
    pass
def isPasswdCorr(email, passwd):
    pass

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Welcome to 'CDN with WAF' project!</h1>"

@application.route("/signup")
def signup():
    return render_template('register.html')

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
    application.secret_key = 'CDN-with-WAF'
    application.run(host='0.0.0.0', debug=True, port=6081)
