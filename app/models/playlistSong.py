# from datetime import datetime
# from .db import db

# PlaylistSong = db.Table(
#     'playlist_songs',

#     db.Column('id', db.Integer, primary_key=True),
#     db.Column('playlist_id', db.Integer, db.ForeignKey('playlists.id'), nullable=False),
#     db.Column('song_id', db.Integer, db.ForeignKey('songs.id'), nullable=False),
#     db.Column('created_at', db.DateTime, default=datetime.utcnow),
#     db.Column('updated_at', db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
# )
