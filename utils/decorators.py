from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt

def role_required(*roles):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            claims = get_jwt()
            if claims.get('role') not in roles:
                return jsonify({'msg': 'Access denied'}), 403
            return f(*args, **kwargs)
        return wrapper
    return decorator
