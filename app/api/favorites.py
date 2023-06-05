from flask import Blueprint, jsonify, request
from flask_login import current_user, login_required
from app import db
from app.models import Favorite

favorites_bp = Blueprint('favorites', __name__, url_prefix='/favorites')

@favorites_bp.route('/', methods=['GET'])
@login_required
def get_favorites():
    favorites = Favorite.query.filter_by(user_id=current_user.id).all()
    favorites_data = [favorite.to_dict() for favorite in favorites]
    return jsonify(favorites=favorites_data), 200

@favorites_bp.route('/', methods=['POST'])
@login_required
def add_favorite():
    song_id = request.json.get('song_id')
    favorite = Favorite.query.filter_by(user_id=current_user.id, song_id=song_id).first()
    if favorite:
        return jsonify(message='Song is already in favorites'), 400
    favorite = Favorite(user_id=current_user.id, song_id=song_id)
    db.session.add(favorite)
    db.session.commit()
    return jsonify(message='Song added to favorites'), 201

@favorites_bp.route('/<int:favorite_id>', methods=['PUT'])
@login_required
def update_favorite(favorite_id):
    favorite = Favorite.query.get(favorite_id)
    if not favorite:
        return jsonify(message='Favorite not found'), 404
    if favorite.user_id != current_user.id:
        return jsonify(message='You do not have permission to update this favorite'), 403

    song_id = request.json.get('song_id')
    favorite.song_id = song_id
    db.session.commit()
    return jsonify(message='Favorite updated successfully'), 200

@favorites_bp.route('/<int:favorite_id>', methods=['DELETE'])
@login_required
def remove_favorite(favorite_id):
    favorite = Favorite.query.get(favorite_id)
    if not favorite:
        return jsonify(message='Favorite not found'), 404
    if favorite.user_id != current_user.id:
        return jsonify(message='You do not have permission to delete this favorite'), 403
    db.session.delete(favorite)
    db.session.commit()
    return jsonify(message='Favorite removed successfully'), 200
