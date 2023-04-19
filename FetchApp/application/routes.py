from flask import render_template, jsonify, request, redirect, url_for
import hashlib
from application.models.people import Person
from application import app, service

#ROUTE Landing Page
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if len(path) > 0:
        return 'ERROR 404 %s does not exist' % path
    # return 'Welcome Page' #login template
    return render_template('index.html')

# ROUTE try to login (encrypted for security)
@app.route('/login', methods=['GET', 'POST'])
def try_login():
    error = ""
    if request.method == "POST":
        attempted_email = request.form['emailInput']

        encryptedPassword = hashlib.sha256(
            request.form['passwordInput'].encode('utf-8')
        ).hexdigest()
        return redirect(url_for('success', name=encryptedPassword))
    return render_template('login.html')


# ROUTE for when logged in (encrypted for security just returns encryption of password  > This will be our user matches page)
@app.route('/success/<name>', methods=['GET', 'POST'])
def success(name):
    return 'welcome %s' % name