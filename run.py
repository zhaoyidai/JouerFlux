from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint





db = SQLAlchemy()
ma = Marshmallow()

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jouerflux.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'secret_key'  # Change

db.init_app(app)
ma.init_app(app)
jwt = JWTManager(app)

# register blueprints
from app.routes.firewall import firewall_bp
app.register_blueprint(firewall_bp)

from app.routes.policy import policy_bp
app.register_blueprint(policy_bp)

from app.routes.rule import rule_bp
app.register_blueprint(rule_bp)

from app.errors import errors
app.register_blueprint(errors)

from app.auth import auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')

# Swagger
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swagger_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "JouerFlux API"
    }
)
app.register_blueprint(swagger_blueprint, url_prefix=SWAGGER_URL)


# tester acces swagger.json
@app.route('/test-static')
def test_static():
    return send_from_directory(app.static_folder, 'swagger.json')


if __name__ == '__main__':
    app.run(debug=True)
