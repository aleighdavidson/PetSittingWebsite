from application.models.user import User
from application.models.dog import Dog
from application.models.dog_photos import DogPhoto
from application.models.dog_type import DogType
from application.models.sitter_type import SitterType
from application import db
from sqlalchemy.sql import text


# check login details for a user
def check_login_details(email, password):
    return db.session.query(User).filter_by(email=email, password=password, ).first()


# Add a user without specifying the ID
def add_user(email, password, fname, sname, city, phone, bio):
    # create an sql query that inserts the data
    sql = "INSERT INTO user (first_name, last_name, city, phone, email, password, user_type, bio) VALUES" + \
          "('" + fname + "', '" + sname + "', '" + city + "', '" + phone + "', '" + email + "', '" + password + "', 'Sitter', '" + bio + "');"

    # convert the sql into a text type (alchemy thing...) then execute
    db.session.execute(text(sql))
    db.session.commit()  # also gotta commit so they actually stay on the database
    # return the user that was just added. This works by getting the latest user that was added.
    return db.session.query(User).order_by(User.id.desc()).first()


# Finish the sitter using the user_id and dog_type
# Will UPDATE the user's sitter_type_id to the dog_type selected
def finish_sitter(user_id, dog_type):
    sql = "UPDATE fetchdb.user SET sitter_type_id = " + str(dog_type) + " WHERE id = " + str(user_id) + ";"
    db.session.execute(text(sql))
    db.session.commit()


# Finish the owner and add the dog and photo information
def finish_owner(user_id, dog_name, dog_age, type_id, description, photo):
    # UPDATE user to type "Owner"
    user = get_account_details(user_id)
    user.user_type = "Owner"

    # add the dog into the dog table
    sqlDog = "INSERT INTO fetchdb.dog(user_id, dog_name, dog_age, type_id, description) " \
             "VALUES (" + str(user_id) + ", '" + str(dog_name) + "', " + str(dog_age) + ", " + str(
        type_id) + ", '" + str(description) + "');"

    db.session.execute(text(sqlDog))

    # grab the dog that was just added
    dog = db.session.query(Dog).order_by(Dog.id.desc()).first()

    # add the photo along with the dog's id into the dog_photos table
    sqlPhoto = "INSERT INTO fetchdb.dog_photos(dog_id, photo) VALUES (" + str(dog.id) + ", '" + str(photo) + "');"
    db.session.execute(text(sqlPhoto))

    # commit the changes
    db.session.commit()


def get_account_details(id):
    user = db.session.query(User).filter_by(id=id).first()
    return user


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


def match_sitter(dogtype):
    sitter = db.session.query(User).filter(User.sitter_type_id == dogtype).all()
    return sitter


def get_user_dog(user_id):
    dog = db.session.query(Dog).filter(Dog.user_id == user_id).first()
    return dog


def get_dog_profile(id):
    return db.session.query(Dog).filter_by(id=id).first()


def get_dog_photo(dog_id):
    return db.session.query(DogPhoto).filter_by(dog_id=dog_id).first()
