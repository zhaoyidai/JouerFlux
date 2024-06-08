from flask import Blueprint, request, jsonify
from app import db
from app.models import Policy, Rule
from app.schemas import rule_schema, rules_schema

rule_bp = Blueprint('rule_bp', __name__)


@rule_bp.route('/rule', methods=['POST'])
def create_rule():
    data = request.get_json()
    source = data.get('source')
    policy_id = data.get('policy_id')
    destination = data.get('destination')
    action = data.get('action')
    if not source or not policy_id or not destination or not action:
        return jsonify({'message': 'All fields should be filled'}), 400

    policy = Policy.query.get(policy_id)
    if not policy:
        return jsonify({'message': 'Policy does not exist'}), 400

    rule = Rule(policy_id=policy_id, source=source, destination=destination, action=action)
    db.session.add(rule)
    db.session.commit()
    return rule_schema.jsonify(policy), 201


@rule_bp.route('/rule', methods=['GET'])
def get_rules():
    rules = Rule.query.all()
    if not rules:
        return jsonify({'message': 'no rule'}), 404

    return rules_schema.jsonify(rules), 200


@rule_bp.route('/rule/<int:p_id>', methods=['GET'])
def get_rules(p_id):
    policy = Policy.query.get(p_id)
    if not policy:
        return jsonify({'message': 'Policy does not exist'}), 400

    rules = Rule.query.filter_by(policy_id=p_id).all()
    if not rules:
        return jsonify({'message': 'no rules'}), 404

    return rules_schema.jsonify(rules), 200


@rule_bp.route('/rule/<int:rule_id>', methods=['DELETE'])
def delete_rule(rule_id):
    rule = Rule.query.get_or_404(rule_id)
    db.session.delete(rule)
    db.session.commit()
    return jsonify({'message': f'rule {rule_id} deleted'}), 200
