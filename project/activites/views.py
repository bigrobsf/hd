from flask import redirect, request, render_template, Blueprint, url_for
from project.models import Exercise, Activity, Workout
# from project.tags.forms import ActivityForm, DeleteForm
from project import db
from flask_login import login_required

# tags_blueprint to register in __init__.py
activities_blueprint = Blueprint(
    'activities',
    __name__,
    template_folder='templates'
)