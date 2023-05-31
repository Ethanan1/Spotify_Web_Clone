from datetime import datetime
from app.models import Song, db

seeder_data = [
    {
        'title': 'Song 1',
        'artist': 'Artist 1',
        'album': 'Album 1',
        'duration': 180,
        'cover_photo_url': 'https://example.com/song1.jpg',
        'created_at': datetime.utcnow(),
        'updated_at': datetime.utcnow(),
    },
    {
        'title': 'Song 2',
        'artist': 'Artist 2',
        'album': 'Album 2',
        'duration': 210,
        'cover_photo_url': 'https://example.com/song2.jpg',
        'created_at': datetime.utcnow(),
        'updated_at': datetime.utcnow(),
    },
    {
        'title': 'Song 3',
        'artist': 'Artist 3',
        'album': 'Album 3',
        'duration': 195,
        'cover_photo_url': 'https://example.com/song3.jpg',
        'created_at': datetime.utcnow(),
        'updated_at': datetime.utcnow(),
    },
    # Add more song data dictionaries as needed
]

def seed_songs():
    songs = []
    for data in seeder_data:
        song = Song(
            title=data['title'],
            artist=data['artist'],
            album=data['album'],
            duration=data['duration'],
            cover_photo_url=data['cover_photo_url'],
            created_at=data['created_at'],
            updated_at=data['updated_at'],
        )
        songs.append(song)
        db.session.add(song)
    db.session.commit()

    return songs

# Define the undo method to remove the seeded data
def undo_songs():
    for song in Song.query.all():
        db.session.delete(song)
    db.session.commit()
