from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app import db
from app.models import User

auth_bp = Blueprint('auth_bp', __name__)

# nouveau utilisateur, definir role
@auth_bp.route('/register', methods=['POST'])
def register():

    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role', 'user')
    # default role user

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password, role=role)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created'}), 201


# se connecter pour un token de connexion
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid user or password'}), 401
    # generer token pour utilisateur connecte
    access_token = create_access_token(identity={'username': user.username, 'role': user.role})
    return jsonify(access_token=access_token), 200


# savoir le role d'utilisateur connecte
@auth_bp.route('/role', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


