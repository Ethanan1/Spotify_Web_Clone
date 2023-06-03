# from datetime import datetime
# from .db import db, environment, SCHEMA, add_prefix_for_prod
# from .song import Song
# from .user import User
# from sqlalchemy.sql import func

# class Favorite(db.Model):
#     __tablename__ = 'favorites'

#     if environment == "production":
#         __table_args__ = {'schema': SCHEMA}

#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#     song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)
    # created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    # updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

#     user = db.relationship('User', backref='favorites')
#     song = db.relationship('Song', backref='favorites')

    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "user_id": self.user_id,
    #         "song_id": self.song_id,
    #         "created_at": self.created_at.isoformat(),
    #         "updated_at": self.updated_at.isoformat(),
    #         "user": self.user.to_dict(),
    #         "song": self.song.to_dict(),
    #         # Add other attributes or relationships as needed
    #     }
