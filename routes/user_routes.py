from flask import Blueprint, request, jsonify
from models import db, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from utils.decorators import role_required
from werkzeug.security import generate_password_hash

user_bp = Blueprint('users', __name__)

@user_bp.route('/manager', methods=['POST'])
@jwt_required()
@role_required('Admin')
def add_manager():
    data = request.json
    manager = User(
        username=data['username'],
        password=generate_password_hash(data['password']),
        role='Manager'
    )
    db.session.add(manager)
    db.session.commit()
    return jsonify({}), 201

@user_bp.route('/employee', methods=['POST'])
@jwt_required()
@role_required('Admin')
def add_employee():
    data = request.json
    employee = User(
        username=data['username'],
        password=generate_password_hash(data['password']),
        role='Employee',
        manager_id=data['manager_id']
    )
    db.session.add(employee)
    db.session.commit()
    return jsonify({}), 201

@user_bp.route('/employees', methods=['GET'])
@jwt_required()
@role_required('Manager')
def get_employees():
    identity = get_jwt_identity()
    employees = User.query.filter_by(manager_id=int(identity)).all()
    return jsonify([{'id': e.id, 'username': e.username, 'status': e.role} for e in employees])

@user_bp.route('/all', methods=['GET'])
@jwt_required()
@role_required('Admin')
def view_all_users():
    users = User.query.all()
    return jsonify([
        {
            "id": u.id,
            "username": u.username,
            "role": u.role,
            "manager_id": u.manager_id
        } for u in users
    ])