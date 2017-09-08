import datetime
from project import app, db
from project.models import User, Workout, Activity, Exercise

# w0 = Workout(datetime.datetime.strptime('Aug 1 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 28, 'workout comment', 1)
# w1 = Workout(datetime.datetime.strptime('Aug 4 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 33, 'another workout comment', 1)
# w2 = Workout(datetime.datetime.strptime('Aug 7 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 26, 'this was an intense one', 1)
# w3 = Workout(datetime.datetime.strptime('Aug 10 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 30, 'workout comment', 1)
# w4 = Workout(datetime.datetime.strptime('Aug 13 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 29, 'it was nice and empty', 1)
# w5 = Workout(datetime.datetime.strptime('Aug 15 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 28, 'made it!', 1)
# w6 = Workout(datetime.datetime.strptime('Aug 17 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 31, 'another comment', 1)
# w7 = Workout(datetime.datetime.strptime('Aug 19 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 30, 'so many exercises', 1)
# w8 = Workout(datetime.datetime.strptime('Aug 23 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 27, 'no waiting!', 1)
# w9 = Workout(datetime.datetime.strptime('Aug 24 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 30, 'are we there yet?', 1)
# w10 = Workout(datetime.datetime.strptime('Aug 27 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 31, 'it is happening again', 1)
# w11 = Workout(datetime.datetime.strptime('Aug 30 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 32, 'call me AHnold', 1)

# w0 = Workout(datetime.datetime.strptime('Jul 1 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 28, 'workout comment', 2)
# w1 = Workout(datetime.datetime.strptime('Jul 4 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 33, 'another workout comment', 2)
# w2 = Workout(datetime.datetime.strptime('Jul 7 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 26, 'this was an intense one', 2)
# w3 = Workout(datetime.datetime.strptime('Jul 10 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 30, 'workout comment', 2)
# w4 = Workout(datetime.datetime.strptime('Jul 13 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 29, 'it was nice and empty', 2)
# w5 = Workout(datetime.datetime.strptime('Jul 15 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 28, 'made it!', 2)
# w6 = Workout(datetime.datetime.strptime('Jul 17 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 31, 'another comment', 2)
# w7 = Workout(datetime.datetime.strptime('Jul 19 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 30, 'so many exercises', 2)
# w8 = Workout(datetime.datetime.strptime('Jul 23 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 27, 'no waiting!', 2)
# w9 = Workout(datetime.datetime.strptime('Jul 24 2017  1:33PM', '%b %d %Y %I:%M%p'), 'World Gym SF', 30, 'are we there yet?', 2)
#
# db.session.add_all([w0, w1, w2, w3, w4, w5, w6, w7, w8, w9])
# db.session.commit()

# a1 = Activity(10,110,'test comment',28,1)
# a2 = Activity(12,90,'test comment',28,2)
# a3 = Activity(9,245,'test comment',28,3)
# a4 = Activity(18,250,'test comment',28,4)
# a5 = Activity(13,340,'test comment',28,6)
# a6 = Activity(15,180,'test comment',28,7)
# a7 = Activity(10,160,'test comment',28,8)
# a8 = Activity(11,225,'test comment',28,9)
# a9 = Activity(14,125,'test comment',28,10)
# a10 = Activity(15,90,'test comment',28,11)
# a11 = Activity(13,70,'test comment',28,12)
# a12 = Activity(10,60,'test comment',28,13)
#
# db.session.add_all([a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12])
# db.session.commit()
#
# a1 = Activity(11,110,'test comment',29,1)
# a2 = Activity(13,90,'test comment',29,2)
# a3 = Activity(11,245,'test comment',29,3)
# a4 = Activity(16,250,'test comment',29,4)
# a5 = Activity(14,340,'test comment',29,6)
# a6 = Activity(16,180,'test comment',29,7)
# a7 = Activity(11,160,'test comment',29,8)
# a8 = Activity(10,225,'test comment',29,9)
# a9 = Activity(14,125,'test comment',29,10)
# a10 = Activity(14,90,'test comment',29,11)
# a11 = Activity(14,70,'test comment',29,12)
# a12 = Activity(12,60,'test comment',29,13)
#
# db.session.add_all([a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12])
# db.session.commit()
#
# a1 = Activity(11,110,'test comment',30,1)
# a2 = Activity(14,90,'test comment',30,2)
# a3 = Activity(11,245,'test comment',30,3)
# a4 = Activity(16,250,'test comment',30,4)
# a5 = Activity(13,340,'test comment',30,6)
# a6 = Activity(14,180,'test comment',30,7)
# a7 = Activity(11,160,'test comment',30,8)
# a8 = Activity(11,225,'test comment',30,9)
# a9 = Activity(15,125,'test comment',30,10)
# a10 = Activity(15,90,'test comment',30,11)
# a11 = Activity(15,70,'test comment',30,12)
# a12 = Activity(12,60,'test comment',30,13)
#
# db.session.add_all([a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12])
# db.session.commit()
#
# a1 = Activity(12,110,'test comment',31,1)
# a2 = Activity(14,90,'test comment',31,2)
# a3 = Activity(11,245,'test comment',31,3)
# a4 = Activity(17,250,'test comment',31,4)
# a5 = Activity(14,340,'test comment',31,6)
# a6 = Activity(16,180,'test comment',31,7)
# a7 = Activity(12,160,'test comment',31,8)
# a8 = Activity(10,225,'test comment',31,9)
# a9 = Activity(15,125,'test comment',31,10)
# a10 = Activity(16,90,'test comment',31,11)
# a11 = Activity(16,70,'test comment',31,12)
# a12 = Activity(15,70,'test comment',31,13)
#
# db.session.add_all([a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12])
# db.session.commit()
#
# a1 = Activity(13,110,'test comment',32,1)
# a2 = Activity(15,90,'test comment',32,2)
# a3 = Activity(13,245,'test comment',32,3)
# a4 = Activity(18,250,'test comment',32,4)
# a5 = Activity(13,340,'test comment',32,6)
# a6 = Activity(16,180,'test comment',32,7)
# a7 = Activity(12,160,'test comment',32,8)
# a8 = Activity(11,225,'test comment',32,9)
# a9 = Activity(16,125,'test comment',32,10)
# a10 = Activity(16,90,'test comment',32,11)
# a11 = Activity(15,70,'test comment',32,12)
# a12 = Activity(16,70,'test comment',32,13)
#
# db.session.add_all([a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12])
# db.session.commit()
#
# a1 = Activity(13,110,'test comment',33,1)
# a2 = Activity(15,90,'test comment',33,2)
# a3 = Activity(14,245,'test comment',33,3)
# a4 = Activity(16,250,'test comment',33,4)
# a5 = Activity(14,340,'test comment',33,6)
# a6 = Activity(16,190,'test comment',33,7)
# a7 = Activity(13,160,'test comment',33,8)
# a8 = Activity(12,225,'test comment',33,9)
# a9 = Activity(12,135,'test comment',33,10)
# a10 = Activity(17,90,'test comment',33,11)
# a11 = Activity(16,70,'test comment',33,12)
# a12 = Activity(16,70,'test comment',33,13)
#
# db.session.add_all([a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12])
# db.session.commit()
#
a1 = Activity(13,110,'test comment',34,1)
a2 = Activity(16,90,'test comment',34,2)
a3 = Activity(14,245,'test comment',34,3)
a4 = Activity(18,250,'test comment',34,4)
a5 = Activity(14,340,'test comment',34,6)
a6 = Activity(15,190,'test comment',34,7)
a7 = Activity(14,160,'test comment',34,8)
a8 = Activity(12,225,'test comment',34,9)
a9 = Activity(11,135,'test comment',34,10)
a10 = Activity(12,100,'test comment',34,11)
a11 = Activity(12,80,'test comment',34,12)
a12 = Activity(14,80,'test comment',34,13)

db.session.add_all([a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12])
db.session.commit()

a1 = Activity(12,110,'test comment',35,1)
a2 = Activity(12,100,'test comment',35,2)
a3 = Activity(16,245,'test comment',35,3)
a4 = Activity(20,250,'test comment',35,4)
a5 = Activity(15,340,'test comment',35,6)
a6 = Activity(16,190,'test comment',35,7)
a7 = Activity(15,160,'test comment',35,8)
a8 = Activity(13,225,'test comment',35,9)
a9 = Activity(12,135,'test comment',35,10)
a10 = Activity(12,100,'test comment',35,11)
a11 = Activity(13,80,'test comment',35,12)
a12 = Activity(13,80,'test comment',35,13)

db.session.add_all([a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12])
db.session.commit()

a1 = Activity(13,110,'test comment',36,1)
a2 = Activity(12,100,'test comment',36,2)
a3 = Activity(16,245,'test comment',36,3)
a4 = Activity(15,275,'test comment',36,4)
a5 = Activity(16,340,'test comment',36,6)
a6 = Activity(16,190,'test comment',36,7)
a7 = Activity(16,160,'test comment',36,8)
a8 = Activity(12,225,'test comment',36,9)
a9 = Activity(13,135,'test comment',36,10)
a10 = Activity(13,100,'test comment',36,11)
a11 = Activity(14,80,'test comment',36,12)
a12 = Activity(14,80,'test comment',36,13)

db.session.add_all([a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12])
db.session.commit()

a1 = Activity(13,110,'test comment',37,1)
a2 = Activity(11,100,'test comment',37,2)
a3 = Activity(17,245,'test comment',37,3)
a4 = Activity(16,275,'test comment',37,4)
a5 = Activity(15,340,'test comment',37,6)
a6 = Activity(16,190,'test comment',37,7)
a7 = Activity(17,160,'test comment',37,8)
a8 = Activity(13,225,'test comment',37,9)
a9 = Activity(14,135,'test comment',37,10)
a10 = Activity(14,100,'test comment',37,11)
a11 = Activity(14,80,'test comment',37,12)
a12 = Activity(16,80,'test comment',37,13)

db.session.add_all([a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12])
db.session.commit()
