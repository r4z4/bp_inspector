from flask import Flask
from flask_reports.blueprints.home.home import home_bp
from flask_reports.blueprints.redirect.redirect import redirect_bp
from flask_reports.blueprints.gemma.gemma import gemma_bp
from flask_reports.blueprints.freeform.freeform import freeform_bp
from flask_reports.blueprints.db.db import db_bp

# For CSRF
import os
SECRET_KEY = os.urandom(32)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.register_blueprint(home_bp)
    app.register_blueprint(db_bp)
    app.register_blueprint(gemma_bp, url_prefix="/gemma")
    app.register_blueprint(freeform_bp, url_prefix="/freeform")
    # To handle conflicting "/" routes
    app.register_blueprint(redirect_bp, url_prefix="/redirect")

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)