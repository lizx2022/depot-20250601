from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from config.setting import config_dict
from flask_jwt_extended import JWTManager



db=SQLAlchemy()
jwt=JWTManager()#JWT认证模块实例化


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_dict[config_name])
    #初始货APP
    db.init_app(app)
    # 引入蓝图
    from manage.user import user_bp
    # 注册蓝图
    app.register_blueprint(user_bp)
    jwt.init_app(app)#jwt初始化


    return app



