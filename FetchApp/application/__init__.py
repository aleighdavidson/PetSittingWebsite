# import Flask class from the flask module
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename


user = 'fetch.member'
password = 'member.pass'
host = '127.0.0.1'
port = 3306
database = 'fetchdb'

# create a new instance of Flask and store it in app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(
    user, password, host, port, database)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@host/database_name' app.config[
# 'SQLALCHEMY_DATABASE_URI']=('mysql+pymysql://' + getenv('MYSQL_USER') + ':' + getenv('MYSQL_PASSWORD') + '@' +
# getenv('MYSQL_HOST') + '/' + getenv('MYSQL_DB'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'
app.config['UPLOAD_FOLDER'] = 'application/static/images'


# link our app to the persistence layer
db = SQLAlchemy(app)
