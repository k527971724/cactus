import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # 请求结束后自动提交数据库（将会不再支持)
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    # 追踪对象的修改并且发送信号,这需要额外的内存
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):  # 占位函数，给某些子类重写用的
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = \
        'mysql+pymysql://root:k2931718@localhost:3306/cactus_develop?charset=utf8mb4'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite://'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}