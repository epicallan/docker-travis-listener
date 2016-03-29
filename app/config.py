class Config(object):
    TESTING = False
    BASH = {'FRONTENDAPP': 'deploy-di-express-react.sh',
            'CMSAPP': 'deploy-di-django.sh'}
    PORT = 8888


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
