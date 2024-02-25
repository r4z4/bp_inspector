from flask import Flask
from flask_reports.blueprints.basic.basic import basic_bp
from flask_reports.blueprints.redirect.redirect import redirect_bp
from flask_reports.blueprints.gemma.gemma import gemma_bp
from flask_reports.blueprints.db.db import db_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(basic_bp)
    app.register_blueprint(db_bp)
    app.register_blueprint(gemma_bp, url_prefix="/gemma")
    # To handle conflicting "/" routes
    app.register_blueprint(redirect_bp, url_prefix="/redirect")

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)