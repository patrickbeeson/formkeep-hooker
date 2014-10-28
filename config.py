class Config(object):
    DEBUG = False
    TESTING = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_USERNAME = 'pbeeson@thevariable.com'
    MAIL_PASSWORD = 'Six11BicycleC0'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    ADMINS = ['pbeeson@thevariable.com']


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    DEBUG = False
    MAIL_SERVER = 'smtp.webfaction.com'
    MAIL_USERNAME = 'thevariable'
    MAIL_PASSWORD = 'V@r1able'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
