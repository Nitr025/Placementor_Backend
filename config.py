import os


class Config(object):
    SECRET_KEY = 'sasds9wn'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
#     if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
#         SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace(
#             "postgres://", "postgresql://", 1)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    CORS_HEADERS = 'Content-Type'
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
