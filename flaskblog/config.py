import os

class Config:
    SECRET_KEY = '47c26a29076e776064166cd3259c60ba'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD= os.environ.get('EMAIL_PASS')

    # Add environmental variables
    # $vim ~/.bash_profile
    # Paste in the file:
    # export SECRET_KEY = '47c26a29076e776064166cd3259c60ba'
    # export SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    #
    # If env. variables are exported, you can
    # change SECRET_KEY AND SQLALCHEMY_DATABASE_URI
    # in this file as follows:
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

