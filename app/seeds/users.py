from datetime import datetime
from app.models import User, db
from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text

seeder_data = [
    {
        'email': 'john@example.com',
        'password': 'password1',
        'cover_photo_url': 'https://example.com/cover.jpg',
        'theme': 'dark',
    },
    {

        'email': 'jane@example.com',
        'password': 'password2',
        'cover_photo_url': 'https://example.com/cover.jpg',
        'theme': 'light',
    },
    {

        'email': 'mary@example.com',
        'password': 'password3',
        'cover_photo_url': 'https://example.com/cover.jpg',
        'theme': 'dark',
    },
    {
        'email': 'samuel@example.com',
        'password': 'password4',
        'cover_photo_url': 'https://example.com/cover.jpg',
        'theme': 'light',
    },
    # Add more user data dictionaries as needed
]

def seed_users():
    for data in seeder_data:
        user = User(
            email=data['email'],
            password=data['password'],
            cover_photo_url=data['cover_photo_url'],
            theme=data['theme'],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )
        db.session.add(user)
    db.session.commit()

def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
