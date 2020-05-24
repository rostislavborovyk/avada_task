# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from app.admin import admin
from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app import login_manager
from jinja2 import TemplateNotFound
from app.admin.forms import TopBannerForm
import os


@admin.route('/index')
@login_required
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('base_blueprint.login'))

    return render_template('index.html')


@admin.route('/banners', methods=["GET", "POST"])
@login_required
def banners():
    top_banner_form = TopBannerForm()

    if not current_user.is_authenticated:
        return redirect(url_for('base_blueprint.login'))

    if top_banner_form.validate_on_submit():
        filename = "top_banner.jpg"

        top_banner = request.files["file"]
        
        return redirect(url_for("admin_blueprint.banners"))

    return render_template('index2.html', top_banner_form=top_banner_form)





@admin.route('/')
def route_template():
    if not current_user.is_authenticated:
        return redirect(url_for('base_blueprint.login'))

    try:
        return render_template('index.html')

    except TemplateNotFound:
        return render_template('page-404.html'), 404

    except:
        return render_template('page-500.html'), 500
