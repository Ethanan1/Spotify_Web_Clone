from flask import Blueprint, jsonify, session, request
from app.models import User, db
from app.forms import LoginForm
from app.forms import SignUpForm
from flask_login import current_user, login_user, logout_user, login_required

auth_routes = Blueprint('auth', __name__)


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages

@auth_routes.route('/')
def authenticate():
    """
    Authenticates a user.
    """
    if current_user.is_authenticated:
        return current_user.to_dict()
    return {'errors': ['Unauthorized']}


@auth_routes.route('/login', methods=['POST'])
def login():
    """
    Logs a user in
    """
    form = LoginForm()
    # Get the csrf_token from the request cookie and put it into the
    # form manually to validate_on_submit can be used
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        # Add the user to the session, we are logged in!
        user = User.query.filter(User.email == form.data['email']).first()
        login_user(user)
        return user.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@auth_routes.route('/logout')
def logout():
    """
    Logs a user out
    """
    logout_user()
    return {'message': 'User logged out'}


@auth_routes.route('/signup', methods=['POST'])
def sign_up():
    """
    Creates a new user and logs them in
    """
    data = request.get_json()
    # Check if user with the same email already exists
    user = User.query.filter_by(email=data['email']).first()
    if user:
        return {'message': 'User already exists'}, 400

    # Validate the data received from the request
    if 'username' not in data or 'email' not in data or 'password' not in data:
        return {'message': 'Missing required data'}, 400

    if not data['username']:
        return {'message': 'Username is required'}, 400

    if not data['email']:
        return {'message': 'Email is required'}, 400

    if not data['password']:
        return {'message': 'Password is required'}, 400

    # Create a new user and add to the database
    hashed_password = (data['password'])
    new_user = User(username=data['username'], email=data['email'], hashed_password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    # Log in the new user and return the user's details
    login_user(new_user)
    return new_user.to_dict(), 201



@auth_routes.route('/unauthorized')
def unauthorized():
    """
    Returns unauthorized JSON when flask-login authentication fails
    """
    return {'errors': ['Unauthorized']}, 401
