from datetime import datetime
from app.models import User, db
from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text

seeder_data = [
    {
        'username': 'john_doe',
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john@example.com',
        'password': 'password1',
        'cover_photo_url': 'https://example.com/cover.jpg',
        'theme': 'dark',
    },
    {
        'username': 'jane_smith',
        'first_name': 'Jane',
        'last_name': 'Smith',
        'email': 'jane@example.com',
        'password': 'password2',
        'cover_photo_url': 'https://example.com/cover.jpg',
        'theme': 'light',
    },
    {
        'username': 'mary_johnson',
        'first_name': 'Mary',
        'last_name': 'Johnson',
        'email': 'mary@example.com',
        'password': 'password3',
        'cover_photo_url': 'https://example.com/cover.jpg',
        'theme': 'dark',
    },
    {
        'username': 'samuel_wilson',
        'first_name': 'Samuel',
        'last_name': 'Wilson',
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
            username=data['username'],
            first_name=data['first_name'],
            last_name=data['last_name'],
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
