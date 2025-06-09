from flask import Flask,current_app
from flask_migrate import Migrate
from config.setting import Testing
from manage import create_app,db



app = create_app('development')

Migrate(app,db)
#三步来执行数据库迁移， 1：flask db init   2: flask db migrate  3: flask db upgrade 如没有生成表，就查看看model的内容是否执行。


@app.route('/')
def hello_world():


    # put application's code here
    return 'Hello World!'

str='scrypt:32768:8:1$mxa3EenuOir3dsta$0ba142364ed46f71ead59af8d28a98902d99bca14eba4a2f1822a09b0504fece0781ec09563d0d38a0629038f3d7da0cb4a12dcc36fe39ad05a681a0e55da9c4'
print(len(str))

if __name__ == '__main__':
    app.run()
