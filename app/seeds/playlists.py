from datetime import datetime
from app.models.playlist import Playlist
from app.models.db import db, environment, SCHEMA
from app.models import db
from sqlalchemy.sql import text

seeder_data = [
    {
        'user_id': 1,  # User ID associated with the playlist
        'name': 'My Playlist 1',
        'cover_photo_url': 'https://example.com/playlist1.jpg',
        'created_at': datetime.utcnow(),
        'updated_at': datetime.utcnow(),
    },
    {
        'user_id': 1,
        'name': 'My Playlist 2',
        'cover_photo_url': 'https://example.com/playlist2.jpg',
        'created_at': datetime.utcnow(),
        'updated_at': datetime.utcnow(),
    },
    {
        'user_id': 2,
        'name': 'Another Playlist',
        'cover_photo_url': 'https://example.com/playlist3.jpg',
        'created_at': datetime.utcnow(),
        'updated_at': datetime.utcnow(),
    },
    # Add more playlist data dictionaries as needed
]

def seed_playlists():
    playlists = []
    for data in seeder_data:
        playlist = Playlist(
            user_id=data['user_id'],
            name=data['name'],
            cover_photo_url=data['cover_photo_url'],
            created_at=data['created_at'],
            updated_at=data['updated_at'],
        )
        playlists.append(playlist)
        db.session.add(playlist)
    db.session.commit()

    return playlists

# Define the undo method to remove the seeded data
def undo_playlists():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.playlists RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM playlists"))
        db.session.commit()
