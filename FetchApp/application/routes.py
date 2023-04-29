from flask import render_template, jsonify, request, redirect, url_for, flash
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
from application.forms.DeleteUserForm import DeleteUserForm


# ROUTE Landing Page
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if len(path) > 0:
        return 'ERROR 404 %s does not exist' % path
    return render_template('index.html', pageTitle="Index Page")


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
            return redirect(url_for('account', id=user.id))
        # if unsuccessful, will return an error message along with the login page again
        error = "Incorrect details. Please try a different login"
    return render_template('login.html', error=error, pageTitle="Login Page")



#ROUTE to create account (working with buttons in JS too) just need to fix form posting
@app.route('/createAccount', methods=['GET', 'POST'])
def createAccount():
    return render_template('createAccount.html', pageTitle="Create Account Page")

#ROUTE for finish Account (will sort out js button and posting)
@app.route('/finishAccount', methods=['GET', 'POST'])
def finishAccount():
    return render_template('finishAccount.html', pageTitle="Finish Account Page")

# ROUTE This will be our matches page if login successful > it now returns the user ID associated with login details)
@app.route('/success/<id>', methods=['GET', 'POST'])
def success(id):
    return 'welcome %s' % id


# ROUTE display Account Details
@app.route('/account/<id>', methods=['GET', 'POST', 'DELETE'])
def account(id):
    error=''
    user = service.get_account_details(id)
    if user is None:
        error = 'User does not exist.'
    delete_form = DeleteUserForm()
    if request.method == 'POST':
        service.delete_user(id)
        flash('Account Deleted')
        return redirect(url_for('try_login'))
    return render_template('account.html', delete_form=delete_form, user=user, pageTitle='Account Details', message=error)

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
        flash('Changes successfully saved')
        return redirect(url_for('account', id=id))
    return render_template('edit_user_details_form.html',
                           form=form, user=current_user, pageTitle='Edit User Details', message=error)


@app.route('/editdog/<id>', methods=['GET', 'POST', 'DELETE'])
def edit_dog(id):
    error = ""
    current_dog = service.get_dog_profile(id)
    form = DogForm(obj=current_dog)
    form.dog_type_list.data = current_dog.dog_type
    delete_form = DeleteUserForm()
    if request.method == 'POST':
        form = DogForm(request.form)
        current_dog.dog_name = form.dog_name.data
        current_dog.dog_age = form.dog_age.data
        current_dog.description = form.description.data
        service.save_dog_changes(current_dog)
        flash('Changes successfully saved')
        return redirect(url_for('account', id=current_dog.user.id))
    elif request.method == 'DELETE':
        service.delete_dog(current_dog)
        flash('Dog Removed')
        return redirect(url_for('account', id=id))
    return render_template('edit_dog_details_form.html',
                           form=form, delete_form=delete_form, dog=current_dog,
                           pageTitle='Edit Dog Details', message=error)


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
    photo = service.get_dog_photo(id)
    return render_template('dog_profile.html', dog=dog, photo=photo, message=error)


