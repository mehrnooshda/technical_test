# -*- coding: UTF-8 -*-
import config
from flask import Flask

from app.extensions import ma, db, migrate
from app.api.v1 import api as api_v1
from app.models.ram import RamUsage


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.config['JSON_AS_ASCII'] = False
    app.config['SECRET_KEY'] = 'asdasda secret string'
    ma.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(api_v1, url_prefix='/api/v1')
    return app
