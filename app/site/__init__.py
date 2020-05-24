# -*- encoding: utf-8 -*-
"""
This blueprint contains main page logic
"""

from flask import Blueprint

site = Blueprint(
    'site_blueprint',
    __name__,
    url_prefix='/site',
    template_folder='templates',
    static_folder='static',
)
