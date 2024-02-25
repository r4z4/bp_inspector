from flask import Blueprint, request, render_template, redirect
from pydantic import BaseModel
from flask_reports.blueprints.db.db import DbConn, db_bp
# Create blueprint object
home_bp = Blueprint('basic', __name__, template_folder="home_templates")

class HomeData(BaseModel):
    name: str

@home_bp.route("/")
def index():
    home_data = HomeData(name="Aaron")
    return render_template("/home.html", data=home_data)

@home_bp.route("/basic")
def home():
    colors_res = DbConn.get_colors()
    print(colors_res)
    return "This is basic"

@home_bp.route("/home/<name>")
def home_name(name):
    return f'Hello {name}'

@home_bp.route("/home/template/<name>")
def home_name_tmpl(name):
    return render_template("/home.html", name=name)
