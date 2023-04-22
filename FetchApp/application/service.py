from application.models.user import User
from application.models.dog import Dog
from application.models.dog_type import DogType
from application.models.sitter_type import SitterType
from application import db


# check login details for a user
def check_login_details(email, password):
    return db.session.query(User).filter_by(email=email, password=password, ).first()


def get_account_details(id):
    user = db.session.query(User).filter_by(id=id).first()
    return user


######## TESTING ############
# def get_all_users():
#     return db.session.query(User).all()
#
#
# def get_all_dogs():
#     return db.session.query(Dog).all()
#
#
# def get_all_sitter_types():
#     return db.session.query(SitterType).all()
