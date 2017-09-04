from flask import redirect, request, render_template, Blueprint, url_for, flash
from project.models import Exercise
from project.exercises.forms import ExerciseForm, DeleteForm
from project import db
from project.decorators import ensure_correct_user
from flask_login import login_required

# exercises_blueprint to register in __init__.py
exercises_blueprint = Blueprint(
    'exercises',
    __name__,
    template_folder='templates'
)


@exercises_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        form = ExerciseForm(request.form)
        if form.validate():
            exercise = Exercise(form.name.data)

            db.session.add(exercise)
            db.session.commit()
        else:
            return render_template('exercises/new.html', form=form)
    
    return render_template('exercises/index.html', exercises=Exercise.query.all())


@exercises_blueprint.route('/<int:ex_id>/edit')
@login_required
def edit(ex_id):
    found_exercise = Exercise.query.get_or_404(ex_id)
    form = ExerciseForm(obj=found_exercise)
    return render_template('exercises/edit.html', form=form, exercise=found_exercise)


@exercises_blueprint.route('/new')
@login_required
def new():
    form = ExerciseForm(request.form)
    return render_template('exercises/new.html', form=form)


@exercises_blueprint.route('/show/<int:ex_id>', methods=['GET', 'PATCH', 'DELETE'])
@login_required
def show(ex_id):
    found_exercise = Exercise.query.get_or_404(ex_id)
    if request.method == b'PATCH':
        form = ExerciseForm(request.form)
        if form.validate():
            found_exercise.name = form.name.data

            db.session.add(found_exercise)
            db.session.commit()
            return redirect(url_for('exercises.index'))
        else:
            return render_template(url_for('exercises/edit.html', form=form))

    if request.method == b'DELETE':
        form = DeleteForm(request.form)
        if form.validate():
            db.session.delete(found_exercise)
            db.session.commit()
            return redirect(url_for('exercises.index'))
        else:
            return render_template(url_for('exercises/edit.html', form=form))

    return render_template('exercises/show.html', exercise=found_exercise)

