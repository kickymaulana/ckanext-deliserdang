from flask import Blueprint


deliserdang = Blueprint(
    "deliserdang", __name__)


def page():
    return "Hello, deliserdang!"


deliserdang.add_url_rule(
    "/deliserdang/page", view_func=page)


def get_blueprints():
    return [deliserdang]
