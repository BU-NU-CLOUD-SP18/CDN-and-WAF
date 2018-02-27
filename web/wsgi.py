from FlaskServer import application

if __name__ == "__main__":
    application.config['SECRET_KEY'] = "CDN-with_WAF"
    application.run()