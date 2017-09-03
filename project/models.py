from project import db, bcrypt
from flask_login import UserMixin

class User(db.Model, UserMixin):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    admin = db.Column(db.Boolean)
    workouts = db.relationship('Workout', cascade="all, delete-orphan", backref='user', lazy='dynamic')

    def __init__(self, username, password, first_name, last_name, admin):
        self.username = username
        self.password = bcrypt.generate_password_hash(password).decode('UTF-8')
        self.first_name = first_name
        self.last_name = last_name
        self.admin = admin

    def __repr__(self):
        return "User {} {}'s user name is {}".format(self.first_name, self.last_name,
                                                        self.username)

    # class method to invoke using User.authenticate()    
    @classmethod
    def authenticate(cls, username, password):
        found_user = cls.query.filter_by(username=username).first()
        if found_user:
            authenticated_user = bcrypt.check_password_hash(found_user.password, password)
            if authenticated_user:
                return found_user # return user to store in the session
        return False


exercise_tag_table = db.Table('exercise_tags',
    db.Column('exercise_id', db.Integer, db.ForeignKey('exercises.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
)


class Workout(db.Model):

    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(30))
    date = db.Column(db.DateTime)
    length = db.Column(db.Integer)
    comment = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    exercises = db.relationship('Exercise', cascade="all, delete-orphan", backref='workout', 
                                lazy='dynamic')

    def __init__(self, location, date, length, comment, user_id):
        self.location = location
        self.date = date
        self.length = length
        self.comment = comment
        self.user_id = user_id

    def __repr__(self):
        return "Workout at {} on {} of duration {} minutes. {}.".format(self.location, self.date, 
                                                                self.length, self.comment)


class Exercise(db.Model):

    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    reps = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    comment = db.Column(db.String(50))
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))
    tags = db.relationship('Tag', secondary=exercise_tag_table, backref=db.backref('exercises'))

    def __init__(self, name, reps, weight, comment, workout_id):
        self.name = name
        self.reps = reps
        self.weight = weight
        self.comment = comment
        self.workout_id = workout_id

    def __repr__(self):
        return "{} with {} reps at {} pounds. {}.".format(self.name, self.reps, 
                                                          self.weight, self.comment)

class Tag(db.Model):

    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)

    def __init__(self, text):
        self.text = text
