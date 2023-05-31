from datetime import datetime
from app.models import User, db
from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text

seeder_data = [
    {
        'username': 'demouser',
        'first_name': "Demo",
        'last_name': "LastDemo",
        'email': 'demo@aa.io',
        'password': 'password',
        'cover_photo_url': 'https://example.com/cover.jpg',
        'theme': 'dark',
    },
    {
        'username': 'JaneD',
        'first_name': "Jane",
        'last_name': "Doe",
        'email': 'jane@aa.io',
        'password': 'password',
        'cover_photo_url': 'https://example.com/cover.jpg',
        'theme': 'light',
    },
    {
        'username': 'MaryL',
        'first_name': "Mary",
        'last_name': "Lim",
        'email': 'mary@aa.io',
        'password': 'password',
        'cover_photo_url': 'https://example.com/cover.jpg',
        'theme': 'dark',
    },
    {
        'username': 'Sammy',
        'first_name': "Samuel",
        'last_name': "Do",
        'email': 'samuel@aa.io',
        'password': 'password',
        'cover_photo_url': 'https://example.com/cover.jpg',
        'theme': 'light',
    },
    # Add more user data dictionaries as needed
]

def seed_users():
    users = []
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
        users.append(user)
        db.session.add(user)
    db.session.commit()

def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
