from marshmallow import Schema
from marshmallow import fields as f
from marshmallow import post_load
from .exception import BusinessException


class UserRegisterException(BusinessException):
    ERROR = 'User register exception'

    def __init__(self, message, *args: object) -> None:
        super().__init__(message, *args)

    @property
    def error(self):
        return self.ERROR


class User:
    def __init__(self, username,
                 password, email,
                 oauth_type):
        self.username = username
        self.password = password
        self.email = email
        self.oauth_type = oauth_type


class UserSchema(Schema):
    username = f.Str(data_key='userName')
    password = f.Str(data_key='password')
    email = f.Str()
    oauth_type = f.Str(data_key='authType', default='basic')

    @post_load
    def create(self, data, **kwargs):
        return User(**data)
