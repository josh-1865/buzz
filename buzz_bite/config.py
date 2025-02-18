import os


# class Config:
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'default_secret_key'
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     MAIL_SERVER = 'smtp.googlemail.com'
#     MAIL_PORT = 587
#     MAIL_USE_TLS = True
#     MAIL_USERNAME = os.environ.get('EMAIL_USER')
#     MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER', 'mwell2392@gmail.com')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS', 'your-app-password')
