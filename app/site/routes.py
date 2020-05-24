# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from app.site import site
from app.models import Film
from app import db
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
        "trailer_youtube_id": "6ZfuNTqbHE8",
        "name": film_name,

    }
    # film = Film(
    #     name="Терминатор",
    #     country="США",
    #     composer="Тарантино",
    #     producer="Тарантино",
    #     director="Тарантино",
    #     scenarist="Тарантино",
    #     operator="Тарантино",
    #     genre="боевик",
    #     budget="7.00 млн USD",
    #     time=135
    # )
    # db.session.add(film)
    # db.session.commit()

    film = db.session.query(Film).filter(Film.id == 1).first()

    print(film)
    return render_template("site/film_page.html", payload=payload)
