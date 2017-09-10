# LIFT

This is a simple workout tracking app based on a bodybuilding approach in the "High-Intensity Training" category called "Heavy Duty." Heavy Duty was developed in the late 70's and is still used by many today. Although a number of variations on the approach appeared over time, the classic version is that a person does a full body workout two or three times a week. Each workout consists of one set of a static collection of different exercises, each done to failure. The goal is to increase the number of reps performed up to a point when one would increase the weight.

The app tracks, by user, by workout, the weight and number of reps for each exercise. It also has a comment field for each exercise performed for that workout. All of this can be edited later as needed.

The app displays a chart of work done (reps x weight) for all workouts in the database. Although most of the app is responsive so that the UI is mobile-friendly, the graph is best viewed on larger screens.

## Technologies used

Python  
Flask  
d3  
JavaScript  
jQuery  

Postgres   
SQL   
SQLAlchemy   

Flask Login  
Flask WTF  
Flask Modus  
Flask Bcrypt  

Bootstrap  
Jinja

## To install and run locally

```
# clone this repository

# cd into the hd directory
cd hd

# assumes virtualenv already installed
mkvirtualenv hd

# install required python packages
pip install -r requirements.txt

# create and set up database
createdb hd
python manage.py db upgrade

# start server
python app.py

# Runs in port 5000
# http://localhost:5000/
```

## Future enhancements:

Fix / make a better UI - add navbar with Home, Logout, Chart selection...

Allow the user to export workout data to a csv file for download.

Display a chart for each exercise so that the user can see progress by exercise by workout over a user-specified period of time.

Display a chart that shows workout intensity (total work done / workout length).

Allow a user to all a tag to each exercise indicating degree of difficulty - too light, too heavy, no failure, total failure...

Allow a user to add their own custom tags.

Allow a user to add and select the location.

Allow a user to add their own exercises and thus create their own workout.

Allow a user to press a button at the beginning and end of the workout to determine the workout length. 