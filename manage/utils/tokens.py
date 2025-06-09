'''
token的程序
1：加密  数据  userid
2:算法  python模板  from itsdangrous import
3：秘钥  flask  SECRET_KEY  在config中已经了


使用了flask-jwt-extended-token<UNK>

1:引入flask-jwt-extended import JWMANAGER
2: 实例化一个jwt=JWTManager()
3:在定义app初始化   jwt.init_app(app)
4:在login 生成token   生成jwt assess token 和 refresh token,返回2个token 给客户端

5:在需要登录认证的前面加上装饰器@jwt-required()

6:

'''

