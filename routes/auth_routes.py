from flask import Blueprint, request, jsonify
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'msg': 'User already exists'}), 400
    user = User(username=data['username'], password=generate_password_hash(data['password']), role='Admin')
    db.session.add(user)
    db.session.commit()
    return jsonify({'msg': 'user signup successful'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'msg': 'Bad credentials'}), 401
    access_token = create_access_token(identity=str(user.id), additional_claims={"role": user.role})
    return jsonify(access_token=access_token)

from flask_jwt_extended import jwt_required, get_jwt
from utils.decorators import role_required

@auth_bp.route('/users', methods=['GET'])
@jwt_required()
@role_required('Admin', 'Manager')
def get_all_users():
    users = User.query.all()
    users_list = []
    for user in users:
        users_list.append({
            'id': user.id,
            'username': user.username,
            'role': user.role,
            'manager_id': user.manager_id
        })
    return jsonify(users_list)
