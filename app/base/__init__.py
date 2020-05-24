# -*- encoding: utf-8 -*-
"""
This blueprint contains user reg and auth logic
"""

from flask import Blueprint

base = Blueprint(
    'base_blueprint',
    __name__,
    url_prefix='',
    template_folder='templates',
    static_folder='static'
)
