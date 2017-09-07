import datetime
from project import app, db
from project.models import User, Workout, Activity, Exercise

# w0 = Workout(datetime.datetime.strptime('Aug 1 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 30, 'date insert test 2', 1)
# w1 = Workout(datetime.datetime.strptime('Aug 4 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 30, 'date insert test 2', 1)
# w2 = Workout(datetime.datetime.strptime('Aug 7 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 30, 'date insert test 2', 1)
# w3 = Workout(datetime.datetime.strptime('Aug 10 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 30, 'date insert test 2', 1)
# w4 = Workout(datetime.datetime.strptime('Aug 13 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 30, 'date insert test 2', 1)
# w5 = Workout(datetime.datetime.strptime('Aug 15 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 30, 'date insert test 2', 1)
# w6 = Workout(datetime.datetime.strptime('Aug 17 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 30, 'date insert test 2', 1)
# w7 = Workout(datetime.datetime.strptime('Aug 19 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 30, 'date insert test 2', 1)
# w8 = Workout(datetime.datetime.strptime('Aug 23 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 30, 'date insert test 2', 1)
# w9 = Workout(datetime.datetime.strptime('Aug 24 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 30, 'date insert test 2', 1)
# w10 = Workout(datetime.datetime.strptime('Aug 27 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 30, 'date insert test 2', 1)
# w11 = Workout(datetime.datetime.strptime('Aug 30 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 30, 'date insert test 2', 1)

# db.session.add_all([w0, w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11])
# db.session.commit()

a1 = Activity(13,110,'test comment',27,1)
a2 = Activity(11,110,'test comment',27,2)
a3 = Activity(18,245,'test comment',27,3)
a4 = Activity(18,245,'test comment',27,4)
a5 = Activity(14,340,'test comment',27,6)
a6 = Activity(16,190,'test comment',27,7)
a7 = Activity(9,160,'test comment',27,8)
a8 = Activity(13,245,'test comment',27,9)
a9 = Activity(16,135,'test comment',27,10)
a10 = Activity(14,95,'test comment',27,11)
a11 = Activity(14,80,'test comment',27,12)
a12 = Activity(17,70,'test comment',27,13)

db.session.add_all([a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12])
db.session.commit()
