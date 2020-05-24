# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from app.site import site
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from app import login_manager
from jinja2 import TemplateNotFound


@site.route("/", methods=["GET", "POST"])
def main_page():
    cards = [
        [
            {"img": "card1.jpg", "name": "Ginger and rosa"},
            {"img": "card2.jpg", "name": "Terminator"},
            {"img": "card3.jpg", "name": "Assassin's creed"},
            {"img": "card4.jpg", "name": "Monster hunter"},
        ],
        [
            {"img": "card1.jpg", "name": "Ginger and rosa"},
            {"img": "card2.jpg", "name": "Terminator"},
            {"img": "card3.jpg", "name": "Assassin's creed"},
            {"img": "card4.jpg", "name": "Monster hunter"},
        ],
        [
            {"img": "card1.jpg", "name": "Ginger and rosa"},
            {"img": "card2.jpg", "name": "Terminator"},

        ],

    ]
    payload = {
        "film_cards": cards
    }
    return render_template("site/main_page.html", payload=payload)


@site.route("/film/<film_name>", methods=["GET", "POST"])
def film_page(film_name):
    payload = {
        "name": film_name
    }
    return render_template("site/film_page.html", payload=payload)
