from datetime import timedelta


class Baseconfig(object):
    DEBUG = True
    TESTING = False
    JSON_AS_ASCII =False
    HOST = 'localhost'
    USER = 'root'
    PASSWORD = '392221'
    PORT = '3306'
    DATABASE = 'lizx10'
    DB_URI = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SECRET_KEY = 'AABBCC'
    #jwt-extended，参数
    # jwt 相关配置
    # 加密算法,默认: HS256
    JWT_ALGORITHM = "HS256"
    # 秘钥，默认是flask配置中的SECRET_KEY
    JWT_SECRET_KEY = SECRET_KEY
    # token令牌有效期，单位: 秒/s，默认:　datetime.timedelta(minutes=15) 或者 15 * 60
    JWT_ACCESS_TOKEN_EXPIRES = 60
    # refresh刷新令牌有效期，单位: 秒/s，默认：datetime.timedelta(days=30) 或者 30*24*60*60
    JWT_REFRESH_TOKEN_EXPIRES = 30 * 24 * 60 * 60
    # 设置通过哪种方式传递jwt，默认是http请求头，也可以是query_string，json，cookies
    JWT_TOKEN_LOCATION = "headers"
    # 当通过http请求头传递jwt时，请求头参数名称设置，默认值： Authorization
    JWT_HEADER_NAME = "Authorization"
    # 当通过http请求头传递jwt时，令牌的前缀。
    # 默认值为 "Bearer"，例如：Authorization: Bearer <JWT>
    JWT_HEADER_TYPE = "jwt"







class Development(Baseconfig):
    HOST = 'localhost'
    USER = 'root'
    PASSWORD = '392221'
    PORT = '3306'
    DeBUG = True
    DESCRIBE="dev"
class Production(Baseconfig):
    HOST = 'localhost'
    USER = 'root'
    PASSWORD = '392221'
    PORT = '3306'

    C = "pro"
class Testing(Baseconfig):
    HOST = 'localhost'
    USER = 'root'
    PASSWORD = '392221'
    PORT = '3306'
    DESCRIBE = "test"

config_dict={
    'development':Development,
    'production':Production,
    'testing':Testing
}