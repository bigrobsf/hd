from flask_wtf import FlaskForm
from wtforms import StringField, validators, DateField, DecimalField
from project.models import Tag


class WorkoutForm(FlaskForm):
    date = DateField('Date', [validators.required()])
    location = StringField('Location', [validators.Length(min=1, max=30)])
    length = DecimalField('Workout Length', [validators.NumberRange(min=1, max=60)])
    comment = StringField('Comment', [validators.Length(max=50)])

class EditWorkoutForm(FlaskForm):
    location = StringField('Location', [validators.Length(min=1, max=30)])
    length = DecimalField('Workout Length', [validators.NumberRange(min=1, max=60)])
    comment = StringField('Comment', [validators.Length(max=50)])

class DeleteForm(FlaskForm):
    pass