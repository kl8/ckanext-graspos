from flask import Blueprint


graspos = Blueprint(
    "graspos", __name__)


def page():
    return "Hello, graspos!"


graspos.add_url_rule(
    "/graspos/page", view_func=page)


def get_blueprints():
    return [graspos]
