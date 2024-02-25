from flask import Blueprint, request, render_template, redirect
from flask_reports.blueprints.db.db import DbConn, db_bp
# Create blueprint object
basic_bp = Blueprint('basic', __name__, template_folder="templates")

@basic_bp.route("/")
def index():
    colors_res = DbConn.get_colors()
    print(colors_res)
    return "This is wiggle waggle"

@basic_bp.route("/basic")
def basic():
    return "This is basic"

@basic_bp.route("/basic/<name>")
def basic_name(name):
    return f'Hello {name}'

@basic_bp.route("/basic/template/<name>")
def basic_name_tmpl(name):
    return render_template("basic_tmpl/basic.html", name=name)
