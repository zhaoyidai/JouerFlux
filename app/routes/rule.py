from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.utils import admin_required, paginate_query
from run import db
from app.models import Policy, Rule, Firewall
from app.schemas import rule_schema, rules_schema

rule_bp = Blueprint('rule_bp', __name__)


@rule_bp.route('/rule', methods=['POST'])
@jwt_required()
@admin_required
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
    return rule_schema.jsonify(rule), 201


@rule_bp.route('/rule', methods=['GET'])
@jwt_required()
def get_rules():
    rules = Rule.query.all()
    if not rules:
        return jsonify({'message': 'no rule'}), 404

    return rules_schema.jsonify(rules), 200


@rule_bp.route('/rule/<int:p_id>', methods=['GET'])
@jwt_required()
def get_rules_p(p_id):
    policy = Policy.query.get(p_id)
    if not policy:
        return jsonify({'message': 'Policy does not exist'}), 400

    rules = Rule.query.filter_by(policy_id=p_id).all()
    if not rules:
        return jsonify({'message': 'no rules'}), 404

    return rules_schema.jsonify(rules), 200


@rule_bp.route('/rule/<int:rule_id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_rule(rule_id):
    rule = Rule.query.get_or_404(rule_id)
    db.session.delete(rule)
    db.session.commit()
    return jsonify({'message': f'rule {rule_id} deleted'}), 200


# all rules for a firewall
# add pagination
@rule_bp.route('/rules', methods=['GET'])
@jwt_required()
def get_rules_for_firewall():
    firewall_id = request.args.get('firewall_id', type=int)
    if not firewall_id:
        return jsonify({'message': 'Firewall ID is required'}), 400

    firewall = Firewall.query.get(firewall_id)
    if not firewall:
        return jsonify({'message': 'Firewall not found'}), 404

    rules_query = Rule.query.join(Policy).filter(Policy.firewall_id == firewall_id)
    paginated_rules = paginate_query(rules_query, rules_schema)

    if isinstance(paginated_rules, tuple) and isinstance(paginated_rules[1], int):
        # return response directly with status code
        return paginated_rules

    return jsonify(paginated_rules), 200
