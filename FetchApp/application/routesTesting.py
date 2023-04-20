from flask import render_template, jsonify, request, redirect, url_for
import hashlib
from application import app, service, db
from application.models.user import User
from application.models.dog import Dog
from application.models.dog_photos import DogPhoto
from application.models.dog_type import DogType
from application.models.sitter_type import SitterType
from application.models.sitter_type_link import SitterTypeLink
from application.models.sitter_dog_link import SitterDogLink


@app.route('/users', methods=['GET'])
def show_users():
    error = ""
    users = service.get_all_users()
    print("I'm working")
    if len(users) == 0:
        error = "There are no users to display"
    return render_template('usersTest.html', users=users, message=error)


@app.route('/sitters', methods=['GET'])
def show_sitters():
    error = ""
    sitters = service.get_all_sitter_types()
    print("I'm working")
    if len(sitters) == 0:
        error = "There are no users to display"
    return render_template('sitterTypeTest.html', users=sitters, message=error)

