from flask import Blueprint
from flask_restful import Api ,Resource
#定义蓝图
user_bp = Blueprint('user', __name__, url_prefix='/user')

api = Api(user_bp)

#引入视图
from ..user import view