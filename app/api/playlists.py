from flask import Blueprint, jsonify, request
from flask_login import current_user, login_required
from app import db
from app.models.playlist import Playlist

playlists_bp = Blueprint('playlists', __name__, url_prefix='/playlists')

@playlists_bp.route('/', methods=['GET'])
@login_required
def get_playlists():
    playlists = Playlist.query.filter_by(user_id=current_user.id).all()
    playlists_data = [playlist.to_dict() for playlist in playlists]
    return jsonify(playlists=playlists_data), 200

@playlists_bp.route('/<int:playlist_id>', methods=['GET'])
@login_required
def get_playlist(playlist_id):
    # Get the playlist with the specified ID from the database
    playlist = Playlist.query.get(playlist_id)
    if not playlist:
        return jsonify(message='Playlist not found'), 404

    # Check if the current user has permission to access the playlist
    if playlist.user_id != current_user.id:
        return jsonify(message='You do not have permission to access this playlist'), 403

    # Convert the playlist to a dictionary
    playlist_data = playlist.to_dict()

    return jsonify(playlist=playlist_data), 200


@playlists_bp.route('/', methods=['POST'])
@login_required
def create_playlist():
    name = request.json.get('name')
    playlist = Playlist.query.filter_by(user_id=current_user.id, name=name).first()
    if playlist:
        return jsonify(message='Playlist with that name already exists'), 400
    playlist = Playlist(user_id=current_user.id, name=name)
    db.session.add(playlist)
    db.session.commit()
    return jsonify(message='Playlist created successfully'), 201

@playlists_bp.route('/<int:playlist_id>', methods=['PUT'])
@login_required
def update_playlist(playlist_id):
    playlist = Playlist.query.get(playlist_id)
    if not playlist:
        return jsonify(message='Playlist not found'), 404
    if playlist.user_id != current_user.id:
        return jsonify(message='You do not have permission to update this playlist'), 403
    new_name = request.json.get('name')
    playlist.name = new_name
    db.session.commit()
    return jsonify(message='Playlist updated successfully'), 200

@playlists_bp.route('/<int:playlist_id>', methods=['DELETE'])
@login_required
def delete_playlist(playlist_id):
    playlist = Playlist.query.get(playlist_id)
    if not playlist:
        return jsonify(message='Playlist not found'), 404
    if playlist.user_id != current_user.id:
        return jsonify(message='You do not have permission to delete this playlist'), 403
    db.session.delete(playlist)
    db.session.commit()
    return jsonify(message='Playlist deleted successfully'), 200
