from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app import db
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/', methods=['GET'])
@login_required
def get_users():
    users = User.query.all()
    users_data = [user.to_dict() for user in users]
    return jsonify(users=users_data), 200

@users_bp.route('/<int:user_id>', methods=['GET'])
@login_required
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify(message='User not found'), 404

    return jsonify(user=user.to_dict()), 200

@users_bp.route('/me', methods=['GET'])
@login_required
def get_current_user():
    return jsonify(user=current_user.to_dict()), 200

@users_bp.route('/<int:user_id>', methods=['PUT'])
@login_required
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify(message='User not found'), 404

    # Only allow the logged-in user to update their own details
    if user.id != current_user.id:
        return jsonify(message='Unauthorized'), 401

    email = request.json.get('email')
    password = request.json.get('password')
    cover_photo_url = request.json.get('cover_photo_url')

    user.email = email
    user.password = password
    user.cover_photo_url = cover_photo_url

    db.session.commit()

    return jsonify(message='User updated successfully'), 200

@users_bp.route('/<int:user_id>', methods=['DELETE'])
@login_required
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify(message='User not found'), 404

    # Only allow the logged-in user to delete their own account
    if user.id != current_user.id:
        return jsonify(message='Unauthorized'), 401

    db.session.delete(user)
    db.session.commit()

    return jsonify(message='User deleted successfully'), 200



    # ...
