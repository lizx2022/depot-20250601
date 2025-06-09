from datetime import datetime
from tkinter.font import names

from manage import db
from werkzeug.security import generate_password_hash, check_password_hash
class BaseModel:

     created_at = db.Column(db.DateTime, default=datetime.now)
     updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

class User(db.Model):
    __tablename__ = 't_users'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    _pwd = db.Column(db.String(256), nullable=False)
    nick_name=db.Column(db.String(32))
    phone=db.Column(db.String(11))
    email=db.Column(db.String(32))

    def __repr__(self):
        return "<User %r>" % self.name

    @property
    def password(self):
        return self._pwd

    @password.setter
    def password(self, t_pwd):
        self._pwd = generate_password_hash(t_pwd)
        #生成码超过128位，需要将PWD设置为255

    def check_password(self, t_pwd):
        return check_password_hash(self._pwd, t_pwd)



