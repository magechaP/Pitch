import os

class Config:
    '''Main configuration class'''


    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

    SECRET_KEY = "yang lanti"
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URL')


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://petermagecha:1234@localhost/pitch'
    DEBUG = True

config_options = {
  'development':DevConfig,
  'production':ProdConfig
}            