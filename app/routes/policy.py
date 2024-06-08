from flask import Blueprint, request, jsonify
from app import db
from app.models import Policy
from app.schemas import policy_schema, policies_schema

policy_bp = Blueprint('policy_bp', __name__)

@policy_bp.route('/policy', methods=['POST'])
def create_policy():
    data = request.get_json()
    name = data.get('name')
    firewall_id = data.get('firewall_id')

    if not name or not firewall_id:
        return jsonify({'message': 'Name and firewall ID cannot be empty'}), 400

    policy = Policy(name=name, firewall_id=firewall_id)
    db.session.add(policy)
    db.session.commit()
    return policy_schema.jsonify(policy), 201

@policy_bp.route('/policy', methods=['GET'])
def get_policies():
    policies = Policy.query.all()
    if not policies:
        return jsonify({'message': 'empty table'}), 404

    return policies_schema.jsonify(policies), 200

@policy_bp.route('/policy/<int:id>', methods=['DELETE'])
def delete_policy(id):
    policy = Policy.query.get_or_404(id)
    db.session.delete(policy)
    db.session.commit()
    return jsonify({'message': f'policy {id} deleted'}), 200
