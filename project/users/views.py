from flask import redirect, request, render_template, Blueprint, url_for, flash
from project.models import User
from project.users.forms import UserForm, LoginForm, DeleteForm
from sqlalchemy.exc import IntegrityError
from project import db, bcrypt
from project.decorators import prevent_login_signup, ensure_correct_user
from flask_login import login_user, logout_user, login_required

# users_blueprint to register in __init__.py
users_blueprint = Blueprint(
    'users',
    __name__,
    template_folder='templates'
)