from flask import render_template, jsonify, request, redirect, url_for
import hashlib
from application.models.user import User
from application.models.dog import Dog
from application.models.dog_type import DogType
from application.models.sitter_type import SitterType
from application import app, service


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
    return render_template('login.html', error=error)


# ROUTE This will be our matches page if login successful > it now returns the user ID associated with login details)
@app.route('/success/<id>', methods=['GET', 'POST'])
def success(id):
    return 'welcome %s' % id
