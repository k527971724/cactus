from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config  # 包含四个键值对的字典

db = SQLAlchemy()

# 工厂函数：用不同的配置生成不同的实例
def create_app(config_name):
    app = Flask(__name__)  # __name__是__main__或模块名
    app.config.from_object(config[config_name])  # 配置

    config[config_name].init_app(app)  # init_app内容是pass
    db.init_app(app)

    # 将main蓝本注册到程序上（注册到app上后蓝本才成为程序的一部分）
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
