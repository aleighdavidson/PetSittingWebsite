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


# ROUTE Landing Page
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if len(path) > 0:
        return 'ERROR 404 %s does not exist' % path
    return 'Welcome Page'
    # return render_template('index.html')


# ROUTE try to login (encrypted for security)
@app.route('/login', methods=['GET', 'POST'])
def try_login():
    error = ""
    if request.method == "POST":
        attempted_email = request.form['emailInput']
        # the password typed into the password form, will then be encrypted and checked for same encryption in database
        encrypted_password = hashlib.sha256(
            request.form['passwordInput'].encode('utf-8')
        ).hexdigest()
        user = service.check_login_details(attempted_email, encrypted_password)
        # if statement: user exists will return their ID and success URL
        if user:
            return redirect(url_for('success', id=user.id))
        # if unsuccessful, will return an error message along with the login page again
        error = "Incorrect details. Please try a different login"
    return \
        render_template('header.html', pageTitle="Login Page") + \
        render_template('login.html', error=error) + \
        render_template('footer.html')


# ROUTE This will be our matches page if login successful > it now returns the user ID associated with login details)
@app.route('/success/<id>', methods=['GET', 'POST'])
def success(id):
    return 'welcome %s' % id

# ROUTE display Account Details
@app.route('/account/<id>', methods=['GET', 'POST'])
def account(id):
    error = ""
    user = service.get_account_details(id)
    return render_template('account.html', user=user, message=error)

########## TESTING ################

# @app.route('/users', methods=['GET'])
# def show_users():
#     error = ""
#     users = service.get_all_users()
#     print("I'm working")
#     if len(users) == 0:
#         error = "There are no users to display"
#     return render_template('usersTest.html', users=users, message=error)
#
#
# @app.route('/sitters', methods=['GET'])
# def show_sitters():
#     error = ""
#     sitters = service.get_all_sitter_types()
#     print("I'm working")
#     if len(sitters) == 0:
#         error = "There are no users to display"
#     return render_template('sitterTypeTest.html', users=sitters, message=error)
#
#
# @app.route('/users/dog', methods=['GET'])
# def show_users_dogs():
#     error = ""
#     users = service.get_all_users()
#     dogs = service.get_all_dogs()
#     my_dict = {}
#     for dog in dogs:
#         my_dict[dog.user.id] = dog.dog_name
#     return render_template('usersTest.html', users=users, dogs=dogs, my_dict=my_dict, message=error)
