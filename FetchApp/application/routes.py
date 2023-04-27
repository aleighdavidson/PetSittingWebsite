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
from application.forms.UserForm import UserForm
from application.forms.DogForm import DogForm


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
    return render_template('account.html', user=user, pageTitle='Account Details', message=error)


@app.route('/edituser/<id>', methods=['GET', 'POST'])
def edit_user(id):
    error = ""
    current_user = service.get_account_details(id)
    form = UserForm(obj=current_user)
    if current_user.user_type == "Sitter":
        for i in current_user.sitter_type_link:
            current_sitter_type = i.sitter_type
        form.sitter_type_list.data = current_sitter_type

    if request.method == 'POST':
        form = UserForm(request.form)
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.city = form.city.data
        current_user.phone = form.phone.data
        current_user.email = form.email.data
        current_user.bio = form.bio.data

        service.save_account_changes(current_user)
        updated_user = service.get_account_details(current_user.id)
        return render_template('account.html', user=updated_user, pageTitle='Account Details', message=error)
    return render_template('edit_user_details_form.html',
                           form=form, user=current_user, pageTitle='Edit User Details', message=error)


@app.route('/editdog/<id>', methods=['GET', 'POST'])
def edit_dog(id):
    error = ""
    current_dog = service.get_dog(id)
    form = DogForm(obj=current_dog)
    form.dog_type_list.data = current_dog.dog_type

    if request.method == 'POST':
        form = DogForm(request.form)
        current_dog.dog_name = form.dog_name.data
        current_dog.dog_age = form.dog_age.data
        current_dog.description = form.description.data
        service.save_dog_changes(current_dog)

        updated_user = service.get_account_details(current_dog.user.id)
        return render_template('account.html', user=updated_user, pageTitle='Account Details', message=error)
    return render_template('edit_dog_details_form.html',
                           form=form, dog=current_dog, pageTitle='Edit Dog Details', message=error)


@app.route('/matches/<type_id>')
def matches(type_id):
    # retrieve all dogs of the specified dog type
    dog = service.match_dog(type_id)
    return render_template('matches.html', dog=dog)

# route display dog profile
@app.route('/dog_profile/<id>', methods=['GET'])
def show_dog_profile(id):
    error = ""
    dog = service.get_dog_profile(id)
    return render_template('dog_profile.html', dog=dog, message=error)


# TESTING ################

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
