from flask import Blueprint, request, jsonify
from models import db, LeaveRequest, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from utils.decorators import role_required

leave_bp = Blueprint('leave', __name__)

@leave_bp.route('/request', methods=['POST'])
@jwt_required()
@role_required('Employee')
def submit_leave():
    data = request.json
    identity = get_jwt_identity()
    leave = LeaveRequest(employee_id=int(identity), reason=data['reason'])
    db.session.add(leave)
    db.session.commit()
    print(f"[Email] Leave request submitted by Employee {identity}")
    return jsonify({}), 201

@leave_bp.route('/requests', methods=['GET'])
@jwt_required()
@role_required('Manager')
def view_team_requests():
    identity = get_jwt_identity()
    employees = User.query.filter_by(manager_id=int(identity)).all()
    employee_ids = [e.id for e in employees]
    requests = LeaveRequest.query.filter(LeaveRequest.employee_id.in_(employee_ids)).all()
    return jsonify([{'id': r.id, 'employee_id': r.employee_id, 'status': r.status, 'reason': r.reason} for r in requests])

@leave_bp.route('/request/<int:req_id>', methods=['PATCH'])
@jwt_required()
@role_required('Manager')
def approve_reject_leave(req_id):
    data = request.json
    leave = LeaveRequest.query.get(req_id)
    if leave:
        leave.status = data['status']
        db.session.commit()
        print(f"[Email] Leave request #{req_id} has been {data['status']}")
        return jsonify({})
    return jsonify({'msg': 'Leave request not found'}), 404

@leave_bp.route('/my-requests', methods=['GET'])
@jwt_required()
@role_required('Employee')
def my_requests():
    identity = get_jwt_identity()
    requests = LeaveRequest.query.filter_by(employee_id=int(identity)).all()
    return jsonify([{'id': r.id, 'status': r.status, 'reason': r.reason} for r in requests])
