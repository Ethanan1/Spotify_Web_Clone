from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from .song import Song
from .db import db, environment, SCHEMA, add_prefix_for_prod

db = SQLAlchemy()

class PlaylistSong(db.Model):
    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    playlist = db.relationship('Playlist', backref='playlist_songs')
    song = db.relationship(Song, backref='playlist_songs')
