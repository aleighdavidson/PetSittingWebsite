from application.models.user import User
from application.models.dog import Dog
from application.models.dog_type import DogType
from application.models.sitter_type import SitterType
from application import db

# check login details for a user
def check_login_details(email, password):
    return db.session.query(User).filter_by(email=email, pass_word=password, ).first()
