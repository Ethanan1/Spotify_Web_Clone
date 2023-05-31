import os
from flask import Flask, render_template, request, session, redirect
from flask_cors import CORS
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_login import LoginManager
from app.models import db, User
from app.api.auth import auth_routes
from app.api.favorites import favorites_bp
from app.api.playlists import playlists_bp
from app.api.songs import songs_bp
from app.api.users import users_bp
from app.config import Config

app = Flask(__name__, static_folder="../react-app/build", static_url_path="/")

# VERY IMPORTANT DO NOT REMOVE
app.url_map.strict_slashes = False

# Setup login manager
login = LoginManager(app)
login.login_view = "auth.unauthorized"


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


app.config.from_object(Config)
app.register_blueprint(auth_routes, url_prefix="/api/auth")
app.register_blueprint(favorites_bp, url_prefix="/api/favorites")
app.register_blueprint(playlists_bp, url_prefix="/api/playlists")
app.register_blueprint(songs_bp, url_prefix="/api/songs")
app.register_blueprint(users_bp, url_prefix="/api/users")
db.init_app(app)
Migrate(app, db)

# Application Security
CORS(app)

csrf = CSRFProtect(app)

@app.before_request
def https_redirect():
    if os.environ.get("FLASK_ENV") == "production":
        if request.headers.get("X-Forwarded-Proto") == "http":
            url = request.url.replace("http://", "https://", 1)
            code = 301
            return redirect(url, code=code)

@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        "csrf_token",
        generate_csrf(),
        secure=True if os.environ.get("FLASK_ENV") == "production" else False,
        samesite="Strict" if os.environ.get("FLASK_ENV") == "production" else None,
        httponly=True,
    )
    return response

# Register your routes and other configurations here

if __name__ == "__main__":
    app.run()
