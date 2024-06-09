from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.utils import admin_required
from run import db
from app.models import Policy, Firewall
from app.schemas import policy_schema, policies_schema

policy_bp = Blueprint('policy_bp', __name__)


@policy_bp.route('/policy', methods=['POST'])
@jwt_required()
@admin_required
def create_policy():
    data = request.get_json()
    name = data.get('name')
    firewall_id = data.get('firewall_id')

    if not name or not firewall_id:
        return jsonify({'message': 'Name and firewall ID cannot be empty'}), 400

    firewall = Firewall.query.get(firewall_id)
    if not firewall:
        return jsonify({'message': 'Firewall does not exist'}), 400

    policy = Policy(name=name, firewall_id=firewall_id)
    db.session.add(policy)
    db.session.commit()
    return policy_schema.jsonify(policy), 201


@policy_bp.route('/policy', methods=['GET'])
@jwt_required()
def get_policies():
    policies = Policy.query.all()
    if not policies:
        return jsonify({'message': 'empty table'}), 404

    return policies_schema.jsonify(policies), 200


@policy_bp.route('/policy/<int:id>', methods=['GET'])
@jwt_required()
def get_policies_f(id):
    firewall = Firewall.query.get(id)
    if not firewall:
        return jsonify({'message': 'Firewall does not exist'}), 400

    policies = Policy.query.filter_by(firewall_id=id).all()

    if not policies:
        return jsonify({'message': 'empty table'}), 404

    return policies_schema.jsonify(policies), 200


@policy_bp.route('/policy/<int:id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_policy(id):
    policy = Policy.query.get_or_404(id)
    db.session.delete(policy)
    db.session.commit()
    return jsonify({'message': f'policy {id} deleted'}), 200


# policy template