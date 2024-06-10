from app import db


class Firewall(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    ip_address = db.Column(db.String(120), nullable=False)
    policies = db.relationship('Policy', order_by='Policy.id', back_populates='firewall', cascade="all, delete-orphan")


class Policy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    firewall_id = db.Column(db.Integer, db.ForeignKey('firewall.id'), nullable=False)
    firewall = db.relationship('Firewall', back_populates='policies')
    rules = db.relationship('Rule', order_by='Rule.id', back_populates='policy', cascade="all, delete-orphan")


class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    policy_id = db.Column(db.Integer, db.ForeignKey('policy.id'), nullable=False)
    policy = db.relationship('Policy', back_populates='rules')
    source = db.Column(db.String(120), nullable=False)
    destination = db.Column(db.String(120), nullable=False)
    action = db.Column(db.String(50), nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(50), nullable=False)