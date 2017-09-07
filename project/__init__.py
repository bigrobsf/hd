import csv
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_required
from sqlalchemy import text
# from project.decorators import ensure_correct_user
import os

app = Flask(__name__)
modus = Modus(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/hd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

db = SQLAlchemy(app)

# blueprints must be imported after app initialization
from project.users.views import users_blueprint
from project.workouts.views import workouts_blueprint
from project.exercises.views import exercises_blueprint

# register blueprints with the application
app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(workouts_blueprint, url_prefix='/users/<int:user_id>/workouts')
app.register_blueprint(exercises_blueprint, url_prefix='/exercises')

# redirect on attempt to access a private route
login_manager.login_view = 'users.login'

from project.models import User, Workout, Activity, Exercise

# write a method with the user_loader decorator so that flask_login can find a current_user 
@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


@app.route('/')
def root():
    # return redirect(url_for('users.login'))
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.route('/reports/export/<int:user_id>')
@login_required
# @ensure_correct_user
def export(user_id):
    sql = text("select w.user_id, to_char(w.date, 'YYYY-MM-DD') as date, e.name, w.length, a.reps, a.weight, (a.reps * a.weight) as product from workouts w join activities a on w.id = a.workout_id join exercises e on a.exercise_id = e.id order by w.date, e.id;")
    file_data = db.engine.execute(sql)
    file_name = 'workouts.csv'

    with open(file_name, 'w') as csvfile:
        out = csv.writer(csvfile, delimiter=',')
        out.writerow(['user_id', 'date', 'name', 'length', 'reps', 'weight', 'product'])

        for row in file_data:
            out.writerow([row.user_id, row.date, row.name, row.length, row.reps, row.weight, row.product])
    return file_name
