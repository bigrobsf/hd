from flask import redirect, request, render_template, Blueprint, url_for
from project.models import Exercise, Tag
from project.tags.forms import TagForm, DeleteForm
from project import db
from flask_login import login_required

# tags_blueprint to register in __init__.py
tags_blueprint = Blueprint(
    'tags',
    __name__,
    template_folder='templates'
)