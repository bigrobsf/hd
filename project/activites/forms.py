from flask_wtf import FlaskForm
from wtforms import StringField, validators, DecimalField
from project.models import Activity


class ActivityForm(FlaskForm):
    reps = DecimalField('Reps', [validators.NumberRange(min=0, max=50)])
    weight = DecimalField('Weight', [validators.NumberRange(min=0, max=1000)])
    comment = StringField('Comment', [validators.Length(max=50)])