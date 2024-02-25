from flask import Blueprint, url_for, render_template, redirect

redirect_bp = Blueprint('redirect', __name__, template_folder="templates")

@redirect_bp.route("/")
def index():
        return "This is redirect blueprint."

# Blueprints can track with each other easily
# Here we redirect to the endpoint in a function in basic_bp
@redirect_bp.route("/go_to_basic")
def go_to_basic():
    return redirect(url_for("basic.basic"))