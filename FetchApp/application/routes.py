import os
from flask import render_template, jsonify, request, redirect, url_for, flash, session, make_response
import hashlib
from application import app, service, db
from application.models.user import User
from application.models.dog import Dog
from application.models.dog_photos import DogPhoto
from application.models.dog_type import DogType
from application.models.sitter_type import SitterType
# from application.models.sitter_type_link import SitterTypeLink
# from application.models.sitter_dog_link import SitterDogLink
from application.forms.UserForm import UserForm
from application.forms.DogForm import DogForm
from application.forms.DeleteUserForm import DeleteUserForm
from werkzeug.utils import secure_filename


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

    # request.method is from Flask. It checks the way the route was accessed.
    # If it was through POST it means it was accessed through the form that has method="post"
    # POST sends the input data from the HTML. They are accessed using their name
    # e.g. <input type="email" name="emailInput"> This is accessed using request.form["emailInput"]
    if request.method == "POST":

        # the password typed into the password form, will then be encrypted and checked for same encryption in database
        # e.g. user types test123 as password
        # that gets encrypted to "ecd71870d1963316a97e3ac3408c9835ad8cf0f3c1bc703527c30265534f75ae"
        # we then search the database for a password that matches that encryption
        encrypted_password = hashlib.sha256(
            request.form['passwordInput'].encode('utf-8')
        ).hexdigest()

        # grab a user using the email and encrypted password
        user = service.check_login_details(request.form['emailInput'], encrypted_password)

        # if user exists, then continue. Otherwise, the database didn't find a user, so its incorrect details...
        if user:
            session["userID"] = user.id  # Set a session variable. Name is userID and set it to the users ID.

            return redirect(url_for('matches'))
        # if unsuccessful, will return an error message along with the login page again
        error = "Incorrect details. Please try a different login"
    return render_template('login.html', error=error, pageTitle="Login Page")


@app.route('/logout')  # remove session ID
def logout():
    session.pop("userID", None)
    resp = make_response(render_template('index.html', pageTitle="Index Page"))
    resp.delete_cookie("userID")
    return redirect(url_for('catch_all'))

# ROUTE to create account
@app.route('/createAccount', methods=['GET', 'POST'])
def createAccount():
    error = ""
    if request.method == "POST":

        # showError will be false, unless any of these are true
        # use elif so if one is triggered, no need to search through all of them
        showError = False
        if request.form['emailInput'] == "":
            showError = True
        elif request.form['passwordInput'] == "":
            showError = True
        elif request.form['fnameInput'] == "":
            showError = True
        elif request.form['lnameInput'] == "":
            showError = True
        elif request.form['cityInput'] == "":
            showError = True
        elif request.form['phoneInput'] == "":
            showError = True
        elif request.form['bioInput'] == "":
            showError = True

        if showError:
            error = "Please fill in all details"
        else:  # If user has filled in all details

            # Like before, encrypt the password. Then store in the database
            password = hashlib.sha256(
                request.form['passwordInput'].encode('utf-8')
            ).hexdigest()

            # The service returns the user that was added
            # so put that into a variable to be able to keep track of the id
            addedUser = service.add_user(request.form['emailInput'],
                                         password,
                                         request.form['fnameInput'],
                                         request.form['lnameInput'],
                                         request.form['cityInput'],
                                         request.form['phoneInput'],
                                         request.form['bioInput'])

            session["userID"] = addedUser.id

            return redirect(url_for('finishAccount'))

    return render_template('createAccount.html', error=error, pageTitle="Create Account Page")


# ROUTE for finish Account
@app.route('/finishAccount', methods=['GET', 'POST'])
def finishAccount():
    if request.method == 'POST':
        # used to quickly access the specific breed
        breeds = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}  # Each one is mapped to the database dog type

        # this is found using the submit button
        # depending on the name of the submit button it will have either Sitter or Owner
        if "Sitter" in request.form:
            # created a dictionary to make it much easier to add to each one
            # requires a lot less code than creating each variable and trying to keep track of each one
            questionnaire = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}

            # create a loop that goes 1, 2, 3, 4, 5. That is the name of each of the radial groups
            # the radial groups have 5 values: a,b,c,d,e.
            # I access the value of the radio group and use that as the key for the dictionary
            # Then add one to the value of the key
            for i in range(1, 6):
                questionnaire[request.form[str(i)]] = questionnaire[request.form[str(i)]] + 1

            # max() gives the key with the largest value. So using that gives the option that is most selected
            # then I pass userID from session as well as breed and the service sorts that out
            service.finish_sitter(session["userID"], breeds[max(questionnaire, key=questionnaire.get)])

            return redirect(url_for('matches'))

        elif "Owner" in request.form:
            # for owner, they can upload a picture of their dog
            # I get the files from request that are named "profilePictures"
            # This only works with forms that have enctype="multipart/form-data"
            file = request.files["profilePictures"]

            # store the name and then join it with the os filepath and the UPLOAD_FOLDER specified in __init__.py
            file_name = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))

            # finally pass all that data to the service. It will create all the necessary rows
            service.finish_owner(session["userID"],
                                 request.form["dogName"],
                                 request.form["dogAge"],
                                 breeds[request.form["dogTypes"]],
                                 request.form["description"],
                                 request.files["profilePictures"].filename)

            return redirect(url_for('matches'))

    return render_template('finishAccount.html', pageTitle="Finish Account Page")


# ROUTE display Account Details
@app.route('/account', methods=['GET', 'POST', 'DELETE'])
def account():
    error = ''
    try:  # this try/except is so if you try to go back a page after logging out, log in page is displayed
        user = service.get_account_details(session["userID"])
    except KeyError:
        return redirect(url_for('try_login'))
    if user is None:
        error = 'User does not exist.'
    delete_form = DeleteUserForm()
    if request.method == 'POST':
        service.delete_user(session["userID"])
        flash('Account Deleted')
        return redirect(url_for('try_login'))
    return render_template('account.html', delete_form=delete_form, user=user, pageTitle='Account Details',
                           message=error)


@app.route('/edituser', methods=['GET', 'POST'])
def edit_user():
    error = ""
    try:  # this try/except is so if you try to go back a page after logging out, log in page is displayed
        current_user = service.get_account_details(session["userID"])
    except KeyError:
        return redirect(url_for('try_login'))
    form = UserForm(obj=current_user)
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
        return redirect(url_for('account', id=session["userID"]))
    return render_template('edit_user_details_form.html',
                           form=form, user=current_user, pageTitle='Edit User Details', message=error)


@app.route('/editdog', methods=['GET', 'POST', 'DELETE'])
def edit_dog():
    error = ""
    try:  # this try/except is so if you try to go back a page after logging out, log in page is displayed
        current_user = service.get_account_details(session["userID"])
    except KeyError:
        return redirect(url_for('try_login'))
    current_dog = service.get_user_dog(current_user.id)
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
        return redirect(url_for('account', id=session["userID"]))
    # elif request.method == 'DELETE':
    #     service.delete_dog(current_dog)
    #     flash('Dog Removed')
    #     return redirect(url_for('account', id=session["userID"]))
    return render_template('edit_dog_details_form.html',
                           form=form, delete_form=delete_form, dog=current_dog,
                           pageTitle='Edit Dog Details', message=error)


@app.route('/matches')
def matches():
    # retrieve all dogs of the specified dog type
    try:  # this try/except is so if you try to go back a page after logging out, log in page is displayed
        user = service.get_account_details(session["userID"])
    except KeyError:
        return redirect(url_for('try_login'))
    if user.user_type == "Sitter":
        dog = service.match_dog(user.sitter_type_id)
        print(user)
        print(user.dog)
        sitter = ''
    if user.user_type == "Owner":
        # below is temporary so that owner match page has no error with missing dog=dog
        dog = service.get_user_dog(session["userID"])
        dogtype = dog.type_id
        sitter = service.match_sitter(dogtype)
        print(dogtype)
        print(user)
        # print(user.dog)
    return render_template('matches.html', dog=dog, user=user, sitter=sitter, pageTitle='Matches')


# route display dog profile
@app.route('/dog_profile/<id>', methods=['GET'])
def show_dog_profile(id):
    error = ""
    dog = service.get_dog_profile(id)
    photo = service.get_dog_photo(id)
    return render_template('dog_profile.html', dog=dog, photo=photo, pageTitle=dog.dog_name, message=error)
