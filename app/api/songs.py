from flask import Blueprint, jsonify, request
from flask_login import login_required
from app import db
from app.models import Song

songs_bp = Blueprint('songs', __name__, url_prefix='/songs')

@songs_bp.route('/', methods=['GET'])
@login_required
def get_songs():
    songs = Song.query.all()
    songs_data = [song.to_dict() for song in songs]
    return jsonify(songs=songs_data), 200

@songs_bp.route('/', methods=['POST'])
@login_required
def create_song():
    title = request.json.get('title')
    artist = request.json.get('artist')
    album = request.json.get('album')
    duration = request.json.get('duration')
    cover_photo_url = request.json.get('cover_photo_url')

    song = Song(title=title, artist=artist, album=album, duration=duration, cover_photo_url=cover_photo_url)
    db.session.add(song)
    db.session.commit()

    return jsonify(message='Song created successfully'), 201

@songs_bp.route('/<int:song_id>', methods=['PUT'])
@login_required
def update_song(song_id):
    song = Song.query.get(song_id)
    if not song:
        return jsonify(message='Song not found'), 404

    title = request.json.get('title')
    artist = request.json.get('artist')
    album = request.json.get('album')
    duration = request.json.get('duration')
    cover_photo_url = request.json.get('cover_photo_url')

    song.title = title
    song.artist = artist
    song.album = album
    song.duration = duration
    song.cover_photo_url = cover_photo_url

    db.session.commit()

    return jsonify(message='Song updated successfully'), 200

@songs_bp.route('/<int:song_id>', methods=['DELETE'])
@login_required
def delete_song(song_id):
    song = Song.query.get(song_id)
    if not song:
        return jsonify(message='Song not found'), 404

    db.session.delete(song)
    db.session.commit()

    return jsonify(message='Song deleted successfully'), 200
