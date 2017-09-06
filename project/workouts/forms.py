from flask_wtf import FlaskForm
from wtforms import StringField, validators, DateField, IntegerField
from project.models import Workout


class WorkoutForm(FlaskForm):
    location = StringField('Location', [validators.Length(min=1, max=30)])
    comment = StringField('Comment', [validators.Length(max=50)])
    
class EditWorkoutForm(FlaskForm):
    location = StringField('Location', [validators.Length(min=1, max=30)])
    length = IntegerField('Workout Length', [validators.NumberRange(min=1, max=60)])
    comment = StringField('Comment', [validators.Length(max=50)])

class DeleteForm(FlaskForm):
    pass