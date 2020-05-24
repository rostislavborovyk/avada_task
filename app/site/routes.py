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
            {"img": "card1.jpg", "name": "Ginger and rosa", "link": "film/4"},
            {"img": "card2.jpg", "name": "Terminator", "link": "film/3"},
            {"img": "card3.jpg", "name": "Assassin's creed", "link": "film/5"},
            {"img": "card4.jpg", "name": "Monster hunter", "link": "film/6"},
        ],
        [
            {"img": "card1.jpg", "name": "Ginger and rosa", "link": "film/4"},
            {"img": "card2.jpg", "name": "Terminator", "link": "film/3"},
            {"img": "card3.jpg", "name": "Assassin's creed", "link": "film/5"},
            {"img": "card4.jpg", "name": "Monster hunter", "link": "film/6"},
        ],
        [
            {"img": "card1.jpg", "name": "Ginger and rosa", "link": "film/4"},
            {"img": "card2.jpg", "name": "Terminator", "link": "film/3"},

        ],

    ]
    payload = {
        "film_cards": cards
    }
    return render_template("site/main_page.html", payload=payload)


@site.route("/film/<int:film_id>", methods=["GET", "POST"])
def film_page(film_id):
    # film_descr = "Киноадаптация популярной игры Monster Hunter, первая часть которой дебютировала в 2004-м году. Помимо нашего мира существует ещё один: мир опасных и могущественных монстров, которые управляют своей реальностью со смертоносной свирепостью. Когда лейтенант Натали Артемис (Милла Йовович) вместе со своими верными солдатами телепортируется из нашего измерения во вселенную чудовищ, она сталкивается с шокирующей правдой. Вступив в войну с гигантскими и невероятно сильными врагами, Артемис решает объединиться с таинственным человеком – Охотником (Тони Джа), который нашёл способ дать отпор монстрам."
    # film = Film(
    #     name="Охотник на монстров",
    #     country="США",
    #     composer="Пол У. С. Андерсон",
    #     producer="Пол У. С. Андерсон",
    #     director="Пол У. С. Андерсон",
    #     scenarist="Пол У. С. Андерсон",
    #     operator="Пол У. С. Андерсон",
    #     genre="фентези",
    #     budget="6.00 млн USD",
    #     time=117,
    #     description=film_descr,
    #     yt_trailer_id="vwdcpWLUI1c"
    # )
    # db.session.add(film)
    # db.session.commit()

    film = db.session.query(Film).filter(Film.id == int(film_id)).first()
    if film is None:
        return "No such film"
    payload = {
        "name": film.name,
        "composer": film.composer,
        "producer": film.producer,
        "director": film.director,
        "scenarist": film.scenarist,
        "operator": film.operator,
        "genre": film.genre,
        "budget": film.budget,
        "time": film.time,
        "description": film.description,
        "yt_trailer_id": film.yt_trailer_id,
    }

    return render_template("site/film_page.html", payload=payload)
