from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    cover_photo_url = db.Column(db.String(255), nullable=True, default="https://res.cloudinary.com/dtzv3fsas/image/upload/v1684125923/SpotifyClone/black-outline-avatar-silhouette-default-260nw-610982348_ifydtq.jpg")
    theme = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    playlists = db.relationship("Playlist", back_populates="user")
    # favorites = db.relationship('Favorite', backref='user')

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "cover_photo_url": self.cover_photo_url,
            "theme": self.theme,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
