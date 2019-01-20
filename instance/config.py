import os


class Config(object):
    "parent configuration class"
    DEBUG = True
    DATABASE_URL = os.getenv("DATABASE_URL")


class DevelopmentConfig(Config):
    "Configurations for Development"
    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing,"""
    TESTING = True
    DEBUG = True
    DATABASE_URL = os.getenv("DATABASE_TEST_URL")


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
}
