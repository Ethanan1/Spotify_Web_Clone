from datetime import datetime
from app.models import Favorite, db
from sqlalchemy.sql import text
from app.models.db import db, environment, SCHEMA

seeder_data = [
    {
        'user_id': 1,
        'song_id': 1,
        'created_at': datetime.utcnow(),
        'updated_at': datetime.utcnow(),
    },
    {
        'user_id': 1,
        'song_id': 2,
        'created_at': datetime.utcnow(),
        'updated_at': datetime.utcnow(),
    },
    {
        'user_id': 2,
        'song_id': 3,
        'created_at': datetime.utcnow(),
        'updated_at': datetime.utcnow(),
    },
    # Add more favorites data dictionaries as needed
]

def seed_favorites():
    favorites = []
    for data in seeder_data:
        favorite = Favorite(
            user_id=data['user_id'],
            song_id=data['song_id'],
            created_at=data['created_at'],
            updated_at=data['updated_at'],
        )
        favorites.append(favorite)
        db.session.add(favorite)
    db.session.commit()

    return favorites

# Define the undo method to remove the seeded data
def undo_favorites():
    for favorite in Favorite.query.all():
        db.session.delete(favorite)
    db.session.commit()
