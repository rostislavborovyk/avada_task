"""
Models are located in one top level file to provide access to models for all blueprints
"""

from flask_login import UserMixin
from sqlalchemy import Binary, Column, Integer, String, Boolean

from app import db, login_manager

from app.base.util import hash_pass


class User(db.Model, UserMixin):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    username = Column(String(60), unique=True)
    email = Column(String(60), unique=True)
    password = Column(Binary)
    is_admin = Column(Boolean)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            if property == 'password':
                value = hash_pass(value)  # we need bytes here (not plain str)

            setattr(self, property, value)

    def __repr__(self):
        return str(self.username)


class Film(db.Model):
    __tablename__ = 'Film'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), unique=True)
    country = Column(String(60))
    composer = Column(String(60))
    producer = Column(String(60))
    director = Column(String(60))
    scenarist = Column(String(60))
    operator = Column(String(60))
    genre = Column(String(60))
    budget = Column(String(60))
    time = Column(Integer)


@login_manager.user_loader
def user_loader(id):
    return User.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = User.query.filter_by(username=username).first()
    return user if user else None
