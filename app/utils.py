from functools import wraps
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request


# nouveau decorator, determiner si un user a un role admin
def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_identity()
        if claims['role'] != 'admin':
            return jsonify({'message': 'Admins only!'}), 403
        return fn(*args, **kwargs)

    return wrapper


# pagination
def paginate_query(query, schema):
    # page actuelle
    page = request.args.get('page', 1, type=int)
    # nb elements dans une page
    per_page = request.args.get('per_page', 5, type=int)
    # function paginate dans sqlalchemy
    paginated = query.paginate(page=page, per_page=per_page, error_out=False)

    if page > paginated.pages:
        return jsonify({'message': 'Page number out of range'}), 404

    return {
        'items': schema.dump(paginated.items),
        'per page': per_page,
        'total': paginated.total,
        'pages': paginated.pages,
        'current_page': paginated.page
    }
