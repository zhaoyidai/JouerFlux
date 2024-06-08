from . import db

class Firewall(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    ip_address = db.Column(db.String(120), nullable=False)
    policies = db.relationship('Policy', order_by='Policy.id', back_populates='firewall')

class Policy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    firewall_id = db.Column(db.Integer, db.ForeignKey('firewall.id'), nullable=False)
    firewall = db.relationship('Firewall', back_populates='policies')
    rules = db.relationship('Rule', order_by='Rule.id', back_populates='policy')

class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    policy_id = db.Column(db.Integer, db.ForeignKey('policy.id'), nullable=False)
    policy = db.relationship('Policy', back_populates='rules')
    source = db.Column(db.String(120), nullable=False)
    destination = db.Column(db.String(120), nullable=False)
    protocol = db.Column(db.String(50), nullable=False)
    port = db.Column(db.Integer, nullable=False)
    action = db.Column(db.String(50), nullable=False)
