from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.utils import admin_required
from run import db
from app.models import Policy, Firewall, Rule
from app.schemas import policy_schema, policies_schema

policy_bp = Blueprint('policy_bp', __name__)

# policy templates with example rules
POLICY_TEMPLATES = {
    'basic': [
        {'source': 'a', 'destination': 'b', 'action': 'allow'},
        {'source': 'b', 'destination': 'a', 'action': 'allow'},
        {'source': 'e', 'destination': 'any', 'action': 'deny'},
    ],
    'strict': [
        {'source': 'any', 'destination': 'i', 'action': 'allow'},
        {'source': 'b', 'destination': 'a', 'action': 'deny'},
        {'source': 'e', 'destination': 'b', 'action': 'deny'},
    ]
}


# add new policy, admin, with template or not
@policy_bp.route('/policy', methods=['POST'])
@jwt_required()
@admin_required
def create_policy():
    data = request.get_json()
    name = data.get('name')
    firewall_id = data.get('firewall_id')
    template = data.get('template')  # basic/strict

    if not name or not firewall_id:
        return jsonify({'message': 'Name and firewall ID cannot be empty'}), 400

    firewall = Firewall.query.get(firewall_id)
    if not firewall:
        return jsonify({'message': 'Firewall does not exist'}), 400

    if template and template not in POLICY_TEMPLATES:
        # verifier nom de template existe
        return jsonify({'message': 'Invalid template'}), 400

    policy = Policy(name=name, firewall_id=firewall_id)
    db.session.add(policy)
    db.session.commit()

    # Default : pas de template
    # Add rules from the selected template to the policy
    if template:
        # ajouter tous les regles dans template
        for rule_data in POLICY_TEMPLATES[template]:
            rule = Rule(source=rule_data["source"],
                        destination=rule_data["destination"],
                        action=rule_data["action"],
                        policy_id=policy.id)
            db.session.add(rule)
    db.session.commit()

    return policy_schema.jsonify(policy), 201


# Liste des politiques pour un firewall, user role
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


# Supprimer politique a partir d'un id, admin
@policy_bp.route('/policy/<int:id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_policy(id):
    policy = Policy.query.get_or_404(id)
    db.session.delete(policy)
    db.session.commit()
    return jsonify({'message': f'policy {id} deleted'}), 200
