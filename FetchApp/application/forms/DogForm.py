from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from application.models.dog_type import DogType


class DogForm(FlaskForm):
    dog_name = StringField("Your Dog's Name")
    dog_age = StringField("Your Dog's Age")
    description = TextAreaField('A bit about your dog')
    dog_type_list = QuerySelectField(
        'Type of Dog',
        query_factory=lambda: DogType.query,
        allow_blank=False,
        get_label='type_name'
    )
    submit = SubmitField('Save Changes')
