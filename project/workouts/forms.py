from flask_wtf import FlaskForm
from wtforms import StringField, validators, DateField, DecimalField, FormField
from project.models import Workout, Activity, Exercise


class WorkoutForm(FlaskForm):
    location = StringField('Location', [validators.Length(min=1, max=30)])
    comment = StringField('Comment', [validators.Length(max=50)])

class ActivityForm(FlaskForm):
    reps = DecimalField('Reps', [validators.NumberRange(min=0, max=50)])
    weight = DecimalField('Weight', [validators.NumberRange(min=0, max=1000)])
    comment = StringField('Comment', [validators.Length(max=50)])
    
class EditWorkoutForm(FlaskForm):
    location = StringField('Location', [validators.Length(min=1, max=30)])
    length = DecimalField('Workout Length', [validators.NumberRange(min=1, max=60)])
    comment = StringField('Comment', [validators.Length(max=50)])
    activities = [FormField(ActivityForm, e.name) for e in Exercise.query.all()]

class DeleteForm(FlaskForm):
    pass