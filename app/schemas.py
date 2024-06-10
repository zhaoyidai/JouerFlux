from run import ma
from .models import Firewall, Policy, Rule


# eviter serialization manuellement
class FirewallSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Firewall
        load_instance = True


class PolicySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Policy
        load_instance = True


class RuleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Rule
        load_instance = True


firewall_schema = FirewallSchema()
firewalls_schema = FirewallSchema(many=True)
policy_schema = PolicySchema()
policies_schema = PolicySchema(many=True)
rule_schema = RuleSchema()
rules_schema = RuleSchema(many=True)
