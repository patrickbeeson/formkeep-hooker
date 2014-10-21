class Config(object):
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_USERNAME = 'pbeeson@thevariable.com'
    MAIL_PASSWORD = 'Six11BicycleC0'
    MAIL_PORT = 465
    MAIL_USE_SSL = True


class DevelopmentConfig(Config):
    DEBUG = True
