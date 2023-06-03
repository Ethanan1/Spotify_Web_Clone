from datetime import datetime
from sqlalchemy import Time
from .db import db
from sqlalchemy.sql import func

class Song(db.Model):
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    artist = db.Column(db.String(255))
    album = db.Column(db.String(255))
    duration = db.Column(db.Integer, nullable=False)
    cover_photo_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    playlists = db.relationship('Playlist', secondary='playlist_songs', back_populates='songs')

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "artist": self.artist,
            "album": self.album,
            "duration": str(self.duration),  # Convert Time object to string for JSON serialization
            "cover_photo_url": self.cover_photo_url,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
