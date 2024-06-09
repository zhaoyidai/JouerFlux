from flask import Blueprint, request, jsonify
from run import db
from app.models import Firewall
from app.schemas import firewall_schema, firewalls_schema
from flask_jwt_extended import jwt_required
from app.utils import admin_required

firewall_bp = Blueprint('firewall_bp', __name__)


@firewall_bp.route('/', methods=['GET'])
def init_firewall():
    db.create_all()
    example_f = Firewall(name='Example1', ip_address='192.168.0.1')
    db.session.add(example_f)
    db.session.commit()
    return "init database"


@firewall_bp.route('/firewall', methods=['POST'])
@jwt_required()
@admin_required
def create_firewall():
    data = request.get_json()
    name = data.get('name')
    ip_address = data.get('ip_address')

    if not name or not ip_address:
        return jsonify({'message': 'Name and IP address cannot be empty'}), 400

    firewall = Firewall(name=name, ip_address=ip_address)
    db.session.add(firewall)
    db.session.commit()
    return firewall_schema.jsonify(firewall), 201


@firewall_bp.route('/firewall', methods=['GET'])
def get_firewalls():
    firewalls = Firewall.query.all()
    if not firewalls:
        return jsonify({'message': 'empty table'}), 404

    return firewalls_schema.jsonify(firewalls), 200


@firewall_bp.route('/firewall/<int:id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_firewall(id):
    firewall = Firewall.query.get_or_404(id)
    db.session.delete(firewall)
    db.session.commit()
    return jsonify({'message': f'firewall {id} deleted'}), 200


# search firewalls by IP address
@firewall_bp.route('/firewall/search', methods=['GET'])
@jwt_required()
def search_firewalls_by_ip():
    ip_address = request.args.get('ip_address')
    if not ip_address:
        return jsonify({'message': 'IP address is required to search'}), 400

    firewalls = Firewall.query.filter_by(ip_address=ip_address).all()
    if not firewalls:
        return jsonify({'message': 'No firewalls found for this IP address'}), 404

    return firewalls_schema.jsonify(firewalls), 200
