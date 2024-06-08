from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jouerflux.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)

    from .routes.firewall import firewall_bp
    app.register_blueprint(firewall_bp)

    from .routes.policy import policy_bp
    app.register_blueprint(policy_bp)

    from .routes.rule import rule_bp
    app.register_blueprint(rule_bp)

    from .errors import errors
    app.register_blueprint(errors)

    return app
