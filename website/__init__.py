from flask import Flask

def create_app():
    app = Flask(__name__)
    #creates a secrete key for the app
    app.config['SECRET_KEY'] = 'sal;kdf;laskjdf;lasnc;alsncd;asl sc, salkdnf;laskdnf'  

    return app
      