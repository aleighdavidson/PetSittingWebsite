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


def get_dog(id):
    dog = db.session.query(Dog).filter_by(id=id).first()
    return dog


def save_account_changes(user):
    db.session.add(user)
    db.session.commit()


def save_dog_changes(dog):
    db.session.add(dog)
    db.session.commit()


def delete_user(id):
    db.session.query(User).filter_by(id=id).delete()
    db.session.commit()


def delete_dog(dog):
    db.session.query(Dog).filter_by(id=dog.id).delete()
    db.session.commit()


def match_dog(type_id):
    dog = db.session.query(Dog).filter(Dog.type_id == type_id).all()
    # print(dog)
    # for x in dog:
    #     print(x)
    #     print(x.dog_name)
    return dog

# TESTING ############
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
