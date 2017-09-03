from flask import redirect, request, render_template, Blueprint, url_for, flash
from project.models import User, Exercise, Tag
from project.messages.forms import ExerciseForm, DeleteForm
from project import db
from project.decorators import ensure_correct_user
from flask_login import login_required

# exercises_blueprint to register in __init__.py
exercises_blueprint = Blueprint(
    'exercises',
    __name__,
    template_folder='templates'
)