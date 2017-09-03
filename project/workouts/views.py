from flask import redirect, request, render_template, Blueprint, url_for, flash
from project.models import User, Workout, Exercise
from project.messages.forms import WorkoutForm, DeleteForm
from project import db
from project.decorators import ensure_correct_user
from flask_login import login_required

# workouts_blueprint to register in __init__.py
workouts_blueprint = Blueprint(
    'workouts',
    __name__,
    template_folder='templates'
)