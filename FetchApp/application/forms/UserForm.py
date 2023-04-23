from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, Email

from application.models.sitter_type import SitterType


class UserForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(message="First name required")])
    last_name = StringField('Last Name', validators=[DataRequired(message="First name required")])
    city = StringField('City')
    phone = StringField('Phone Number')
    email = StringField('Email Address', validators=[DataRequired(), Email(message="Please enter a valid email address")])
    bio = StringField('Bio')
    sitter_type_list = QuerySelectField(
        'Sitter Type',
        query_factory=lambda: SitterType.query,
        allow_blank=False,
        get_label='sitter_type'
    )
    submit = SubmitField('Save Changes')