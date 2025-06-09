import re

from click import password_option
from flask.views import MethodView
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from flask_restful import Resource,reqparse,inputs
from flask import request
from flask_restful.inputs import regex
from jinja2.runtime import identity
from sqlalchemy.orm import session


from ..user import user_bp,api
#引入models ,要不然就models 就是独立的，没有被执行。如果 APP中，他们从上向下执行，会执行到

from manage import db,models
from manage.utils.message import to_dict_msg


#定义视图类
class UserView(Resource):
    def get(self):
        return {"status": 200, "result":"success"}
    def post(self):
        #restful 数据解释===后端数据验证。使用reqparse   ：实施化一个reqparse 2:添加要解释的数据 add_argument  3:数据解释 parse
        # parser = reqparse.RequestParser()
        # parser.add_argument("name",type=str,required=True,help="用户名有误")
        # parser.add_argument("age",type=int,required=True,help="年龄输入有误 ",default=18)
        # parser.add_argument("phone",type=regex(r'^1\d{10}$'),required=True,help="手机号格式不对")
        # parser.add_argument("email",type=regex(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$'),help="邮箱格式不对")
        # args = parser.parse_args()
        name = request.form.get('name')
        password = request.form.get("password")
        re_password = request.form.get("re_password")
        phone = request.form.get("phone")
        email = request.form.get("email")
        nick_name = request.form.get("nick_name")
        print(name,password,re_password,phone,email,nick_name)

        if not all([name,password,re_password]):
            print ("数据不完整")

            return to_dict_msg(10000)

        if len(name)<2:
            print("name is not good")
            return to_dict_msg(10011)

        if len(password)<2:
            print("password is not good")
            return to_dict_msg(10012)



        if password != re_password:
            print("repassword isnot  equal")
            return to_dict_msg(10013)

        if not re.match(r'0?(13|14|15|17|18|19)[0-9]{9}$', phone):
            print("phone is not  good")
            return to_dict_msg(10014)

        if not re.match(r"^\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}",email):
            print("email is not good")
            return to_dict_msg(10015)

        print ("数据验证OK")
        user = db.session.query(models.User).filter(models.User.name==name).first()
        print (user)
        if user:

             return to_dict_msg(10016)

        try:
            user1=models.User(name=name,password=password,nick_name=nick_name,phone=phone,email=email)
                #添加用户时要在一行内完成，不能换行

            db.session.add(user1)

            db.session.commit()
            return to_dict_msg(200)

        except Exception :
            return to_dict_msg(2000)




#注册路由
api.add_resource(UserView, '/register',endpoint='v_register')

@user_bp.route('/login',methods=['POST'])
def login():
    name=request.form.get("name")
    password=request.form.get("password")
    print(name,password)
    if not all([name,password]):
        return to_dict_msg(10019)
    if len(name)>1:
        user1=models.User.query.filter_by(name=name).first()
        if  user1:
            if user1.check_password(password):
                access_token=create_access_token(identity=str(user1.id))
                refresh_token=create_refresh_token(identity=str(user1.id))

                return to_dict_msg(200,{"access_token":access_token,"refresh_token":refresh_token})
            return to_dict_msg(10021)
        return to_dict_msg(10020)
    return to_dict_msg(200)


#要在路由之前
@user_bp.route('/info',methods=['GET'])
@jwt_required()
def info():
    identity = get_jwt_identity()
    if identity is None:
        return to_dict_msg(10021)
    return to_dict_msg(10022,msg=identity)




@user_bp.route('/refresh')
@jwt_required(refresh=True  )
def refresh():
    identity1=get_jwt_identity()
    access_token=create_access_token(identity=identity1)
    return to_dict_msg(200,{"access_token":access_token})
#token失效后，可以通过refresh 重新获得token


