from flask import redirect, request, render_template, Blueprint, url_for, flash
from project.models import User, Workout, Activity, Exercise
from project.workouts.forms import WorkoutForm, EditWorkoutForm, DeleteForm
from project import db
from project.decorators import ensure_correct_user
from flask_login import login_required
import datetime

# workouts_blueprint to register in __init__.py
workouts_blueprint = Blueprint(
    'workouts',
    __name__,
    template_folder='templates'
)

@workouts_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def index(user_id):
    if request.method == 'POST':
        form = WorkoutForm(request.form)
        if form.validate():
            date = datetime.datetime.today()
            location = request.form.get('location')
            length = 30
            comment = request.form.get('comment')
            new_workout = Workout(date, location, length, comment, user_id)
            db.session.add(new_workout)
            db.session.commit()

            flash('New workout created.')

            return redirect(url_for('workouts.index', user_id=user_id))
        else:
            return render_template('workouts/new.html', form=form, user_id=user_id)
    else:  
        user = User.query.get(user_id)
        workouts = user.workouts.all()

        return render_template('workouts/index.html', user=user, workouts=workouts)    


@workouts_blueprint.route('/<int:wo_id>/edit')
@login_required
@ensure_correct_user
def edit(user_id, wo_id):
    found_workout = Workout.query.get_or_404(wo_id)
    form = WorkoutForm(obj=found_workout)
    return render_template('workouts/edit.html', form=form, workout=found_workout)


@workouts_blueprint.route('/new')
@login_required
@ensure_correct_user
def new(user_id):
    form = WorkoutForm(request.form)
    return render_template('workouts/new.html', form=form, user_id=user_id)


@workouts_blueprint.route('/show/<int:wo_id>', methods=['GET', 'PATCH', 'DELETE'])
@login_required
@ensure_correct_user
def show(user_id, wo_id):
    found_workout = Workout.query.get_or_404(wo_id)
    if request.method == b'PATCH':
        form = EditWorkoutForm(request.form)
        if form.validate():
            found_workout.location = request.form.get('location')
            found_workout.length = int(request.form.get('length'))
            found_workout.comment = request.form.get('comment')

            db.session.add(found_workout)
            db.session.commit()
            return redirect(url_for('workouts.index', user_id=user_id))
        else:
            return render_template(url_for('workouts/edit.html', form=form, workout=found_workout))

    if request.method == b'DELETE':
        form = DeleteForm(request.form)
        if form.validate():
            db.session.delete(found_workout)
            db.session.commit()
            return redirect(url_for('workouts.index', user_id=user_id))
        else:
            return render_template(url_for('workouts/edit.html', form=form, workout=found_workout))

    return render_template('workouts/show.html', workout=found_workout)

