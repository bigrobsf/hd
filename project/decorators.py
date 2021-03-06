from functools import wraps
from flask import redirect, url_for, session, flash
from flask_login import current_user
from project.models import User


def prevent_login_signup(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if current_user.is_authenticated:
            flash("You are logged in already.")
            return redirect(url_for('users.index'))
        return fn(*args, **kwargs)
    return wrapper


def ensure_correct_user(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        correct_id = kwargs.get('user_id') or kwargs.get('id')
        if correct_id != current_user.id:
            flash("Not Authorized")
            return redirect(url_for('users.index',id=session.get('user_id')))
        return fn(*args, **kwargs)
    return wrapper


def ensure_admin_user(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        admin_user = User.query.get(current_user.id)
        if not admin_user.admin:
            flash("Only admin can modify exercises")
            return redirect(url_for('users.index',id=session.get('user_id')))
        return fn(*args, **kwargs)
    return wrapper

def ensure_correct_or_admin_user(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        admin_user = User.query.get(current_user.id)
        correct_id = kwargs.get('user_id') or kwargs.get('id')
        if not admin_user.admin and correct_id != current_user.id:
            flash("Only user or admin can edit")
            return redirect(url_for('users.index',id=session.get('user_id')))
        return fn(*args, **kwargs)
    return wrapper