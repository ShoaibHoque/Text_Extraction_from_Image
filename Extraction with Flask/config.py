import os
from os import environ

class Config(object):

    DEBUG = False
    TESTING = False

    basedir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = 'shoaib'

    UPLOADS = r'D:\Work\Data Science\Personal\Text_Extraction_from_Image\Extraction with Flask\app\static\uploads'

    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None

class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False 

class DebugConfig(Config):
    DEBUG = False 