# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from flask import Flask, url_for
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from importlib import import_module
# from logging import basicConfig, DEBUG, getLogger, StreamHandler
from app.config import Config
import pymysql

# from os import path

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
pymysql.install_as_MySQLdb()


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)


def register_blueprints(app):
    # for module_name in ('base', 'home'):
    #     module = import_module('app.{}.routes'.format(module_name))
    #     app.register_blueprint(module.blueprint)

    base = import_module("app.base.routes").base
    app.register_blueprint(base)

    admin = import_module("app.admin.routes").admin
    app.register_blueprint(admin)

    site = import_module("app.site.routes").site
    app.register_blueprint(site)


def configure_database(app):
    @app.before_first_request
    def initialize_database():

        """  Creates db tables before first request to this instance of the application"""
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def create_app(config_class=Config, selenium=False):
    app = Flask(__name__, static_folder='base/static')
    app.config.from_object(config_class)
    if selenium:
        app.config['LOGIN_DISABLED'] = True
    register_extensions(app)
    register_blueprints(app)
    configure_database(app)
    return app
