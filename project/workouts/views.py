from flask import redirect, request, render_template, Blueprint, url_for, flash
from project.models import User, Workout, Activity, Exercise
from project.workouts.forms import WorkoutForm, EditWorkoutForm, DeleteForm
from project import db
from project.decorators import ensure_correct_user
from flask_login import login_required
from sqlalchemy import desc
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

            activities_to_add = []

            for exercise in Exercise.query.all():
                reps = request.form.get('exercises[reps][{}]'.format(exercise.id)) or 0
                weight = request.form.get('exercises[weight][{}]'.format(exercise.id)) or 0
                comment = request.form.get('exercises[comment][{}]'.format(exercise.id))
                new_activity = Activity(reps, weight, comment, new_workout.id, exercise.id)
                activities_to_add.append(new_activity)
            db.session.add_all(activities_to_add)

            db.session.commit()
            flash('Workout saved.')

            return redirect(url_for('workouts.index', user_id=user_id))
        else:
            return render_template('workouts/new.html', form=form, user_id=user_id)
    else:
        user = User.query.get(user_id)
        workouts = user.workouts.order_by(desc(Workout.date)).all()

        return render_template('workouts/index.html', user=user, workouts=workouts)


@workouts_blueprint.route('/<int:wo_id>/edit')
@login_required
@ensure_correct_user
def edit(user_id, wo_id):
    found_workout = Workout.query.get_or_404(wo_id)
    form = EditWorkoutForm(obj=found_workout)
    return render_template('workouts/edit.html', form=form, workout=found_workout)


@workouts_blueprint.route('/new')
@login_required
@ensure_correct_user
def new(user_id):
    exercises = Exercise.query.all()
    form = WorkoutForm(request.form)
    return render_template('workouts/new.html', exercises=exercises, form=form, user_id=user_id)


@workouts_blueprint.route('/show/<int:wo_id>', methods=['GET', 'PATCH', 'DELETE'])
@login_required
@ensure_correct_user
def show(user_id, wo_id):
    found_workout = Workout.query.get_or_404(wo_id)
    if request.method == b'PATCH':
        form = EditWorkoutForm(request.form)
        if form.validate():
            found_activities = []

            found_workout.location = request.form.get('location')
            found_workout.length = int(float(request.form.get('length'))) or 30
            found_workout.comment = request.form.get('comment')

            db.session.add(found_workout)

            for found_activity in found_workout.activities:
                found_activity.reps = request.form.get('exercises[reps][{}]'.format(found_activity.exercise_id)) or 0
                found_activity.weight = request.form.get('exercises[weight][{}]'.format(found_activity.exercise_id)) or 0
                found_activity.comment = request.form.get('exercises[comment][{}]'.format(found_activity.exercise_id))
                found_activities.append(found_activity)
            db.session.add_all(found_activities)

            db.session.commit()
            return redirect(url_for('workouts.index', user_id=user_id))
        else:
            return render_template('workouts/edit.html', form=form, workout=found_workout)

    if request.method == b'DELETE':
        form = DeleteForm(request.form)
        if form.validate():
            db.session.delete(found_workout)
            db.session.commit()
            return redirect(url_for('workouts.index', user_id=user_id))
        else:
            return render_template('workouts/edit.html', form=form, workout=found_workout)

    return render_template('workouts/show.html', workout=found_workout, user_id=user_id)
