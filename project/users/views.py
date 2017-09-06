from flask import redirect, request, render_template, Blueprint, url_for, flash
from project.models import User
from project.users.forms import NewUserForm, UpdateUserForm, LoginForm, DeleteForm
from sqlalchemy.exc import IntegrityError
from project import db, bcrypt
from project.decorators import prevent_login_signup, ensure_correct_user
from flask_login import login_user, logout_user, login_required, current_user

# users_blueprint to register in __init__.py
users_blueprint = Blueprint(
    'users',
    __name__,
    template_folder='templates'
)


@login_required
@users_blueprint.route('/')
def index():
    found_user = User.query.get_or_404(current_user.id)
    if found_user.admin:
        return render_template('users/index.html', users=User.query.order_by(User.username).all())
    return render_template('users/show.html', user=found_user)

@users_blueprint.route('/signup', methods=['GET', 'POST'])
@prevent_login_signup
def signup():
    form = NewUserForm(request.form)
    if request.method == 'POST':
        if form.validate():
            username = request.form.get('username')
            password = request.form.get('password')
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            admin = request.form.get('admin')

            new_user = User(username, password, first_name, last_name, admin)
            db.session.add(new_user)

            try:
                db.session.commit()
                login_user(new_user)
                flash('User created!')
                return redirect(url_for('users.index'))
            except IntegrityError as err:
                flash('Username already exists.')
                return render_template('users/signup.html', form=form)

    return render_template('users/signup.html', form=form)


@users_blueprint.route('/login', methods=["GET", "POST"])
@prevent_login_signup
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        authenticated_user = User.authenticate(form.username.data, form.password.data)
        if authenticated_user:
            login_user(authenticated_user)
            flash('Login successful.')
            return redirect(url_for('users.index'))
        else:
            flash('Invalid login. Please try again.')
            return redirect(url_for('users.login'))
    return render_template('users/login.html', form=form)


@users_blueprint.route('/<int:id>/edit')
@login_required
@ensure_correct_user
def edit(id):
    found_user = User.query.get_or_404(id)
    form = UpdateUserForm(obj=found_user)
    return render_template('users/edit.html', form=form, user=found_user)


@users_blueprint.route('/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
@login_required
@ensure_correct_user
def show(id):
    found_user = User.query.get_or_404(id)
    if request.method == b'PATCH':
        form = UpdateUserForm(request.form)
        if form.validate():
            found_user.username = request.form.get('username')
            # found_user.password = bcrypt.generate_password_hash(form.password.data).decode('UTF-8')
            found_user.first_name = request.form.get('first_name')
            found_user.last_name = request.form.get('last_name')
            found_user.admin = request.form.get('admin')

            db.session.add(found_user)
            db.session.commit()

            return redirect(url_for('users.index'))

        return render_template('users/edit.html', form=form, user=found_user)
    if request.method == b'DELETE':
        form = DeleteForm(request.form)
        if form.validate():
            db.session.delete(found_user)
            db.session.commit()
            logout_user()
            flash('User Deleted')
            return redirect(url_for('users.login'))
        return render_template('users/edit.html', form=form, user=found_user)

    return render_template('users/show.html', user=found_user)


@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out.')
    return redirect(url_for('users.login'))