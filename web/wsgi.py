from FlaskServer import application

if __name__ == "__main__":
    application.secret_key = 'CDN-with-WAF'
    application.run()