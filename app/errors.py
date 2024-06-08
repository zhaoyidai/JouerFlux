from flask import Blueprint, jsonify

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def not_found_error(error):
    return jsonify({"error": f"Not found, {error}"}), 404


@errors.app_errorhandler(500)
def internal_error(error):
    return jsonify({"error": f"Internal server error, {error}"}), 500
