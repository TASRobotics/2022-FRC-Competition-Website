from flask import Blueprint, render_template, request, flash, redirect, url_for, Response
from .models import Scout
from . import db
import csv

auth = Blueprint('auth', __name__)

@auth.route('/')
@auth.route('/home')
def home():
    return render_template('home.html')

# Data
@auth.route('/data')
def data():
    try:
        data = Scout.query.all()
        return render_template('data.html', data=data)
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

# Scouting
@auth.route('/scout', methods=['GET', 'POST'])
def attempt():
    if request.method == 'POST':
        team = request.form.get('team')
        round = request.form.get('round')
        alliance = request.form.get('alliance')

        # Auton
        taxi = request.form.get('taxi')

        auton_upper_in = request.form.get('auton_upper_in')
        auton_upper_missed = request.form.get('auton_upper_missed')
        auton_upper_unreliable = request.form.get('auton_unreliable_upper')

        auton_lower_in = request.form.get('auton_lower_in')
        auton_lower_missed = request.form.get('auton_lower_missed')
        auton_lower_unreliable = request.form.get('auton_lower_unreliable')

        # Teleop
        tele_upper_in = request.form.get('tele_upper_in')
        tele_upper_missed = request.form.get('tele_upper_missed')
        tele_upper_unreliable = request.form.get('tele_unreliable_upper')

        tele_lower_in = request.form.get('tele_lower_in')
        tele_lower_missed = request.form.get('tele_lower_missed')
        tele_lower_unreliable = request.form.get('tele_lower_unreliable')

        hang = request.form.get('hang')
        win = request.form.get('win')
        cargo_bonus = request.form.get('cargo_bonus')
        hangar_bonus = request.form.get('hangar_bonus')

        new_scout = Scout(team=team, round=round, alliance=alliance, taxi=taxi, 
                          auton_upper_in=auton_upper_in, auton_upper_missed=auton_upper_missed, 
                          auton_upper_unreliable=auton_upper_unreliable, auton_lower_in=auton_lower_in,
                          auton_lower_missed=auton_lower_missed, auton_lower_unreliable=auton_lower_unreliable, 
                          tele_upper_in=tele_upper_in, tele_upper_missed=tele_upper_missed, tele_upper_unreliable=tele_upper_unreliable,
                          tele_lower_in=tele_lower_in, tele_lower_missed=tele_lower_missed, tele_lower_unreliable=tele_lower_unreliable,
                          hang=hang, win=win, cargo_bonus=cargo_bonus, hangar_bonus=hangar_bonus)
        db.session.add(new_scout)
        db.session.commit()
        
    return render_template('scout.html')

# Download the database
@auth.route('/download')
def download():
    data = Scout.query.all()

    # Store it as csv 
    with open(r'C:\Users\22matthewk\Desktop\data.csv', 'w') as s_key:
        csv_out = csv.writer(s_key)

        # Horizontal labels
        csv_out.writerow(["Team", "Round", "Alliance", "Taxi", "A_Upper_In", "A_Upper_Missed", "A_Upper_Unreliable", "A_Lower_In", "A_Lower_Missed", "A_Lower_Unreliable",
                         "T_Upper_In", "T_Upper_Missed", "T_Upper_Unreliable", "T_Lower_In", "T_Lower_Missed", "T_Lower_Unreliable", "Hang", "Cargo", "Hangar"])
        
        # Database data
        data = db.session.query(Scout.team, Scout.round, Scout.alliance, Scout.taxi, Scout.auton_upper_in, Scout.auton_upper_missed, 
                                Scout.auton_upper_unreliable, Scout.auton_lower_in, Scout.auton_lower_missed, Scout.auton_lower_unreliable, 
                                Scout.tele_upper_in, Scout.tele_upper_missed, Scout.tele_upper_unreliable, Scout.tele_lower_in, 
                                Scout.tele_lower_missed, Scout.tele_lower_unreliable, Scout.hang, Scout.cargo_bonus, Scout.hangar_bonus)
        for i in data:
            csv_out.writerow(i)
    return render_template('data.html',data=data)
