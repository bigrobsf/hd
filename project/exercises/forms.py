from flask_wtf import FlaskForm
from wtforms import StringField, validators
from project.models import Exercise

class ExerciseForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=3, max=50)])


class DeleteForm(FlaskForm):
    pass