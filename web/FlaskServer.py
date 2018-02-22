from flask import Flask, render_template
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Welcome to 'CDN with WAF' project!</h1>"

@application.route("/signup")
def signUp():
    return render_template('register.html')

@application.route("/login")
def login():
    return render_template('login.html')

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True, port=6081)
