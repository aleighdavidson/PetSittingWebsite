from application.models.people import Person
from application import db

# check login details for a user
def check_login_details(email, password):
    return db.session.query(Person).filter_by(email=email, pass_word=password, ).first()