from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Scout
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/')
@auth.route('/home')
def home():
    return render_template('home.html')

@auth.route('/scout', methods=['GET', 'POST'])
def scout():
    if request.method == 'POST':
        team = request.form.get('team')
        round = request.form.get('round')
        alliance = request.form.get('alliance')

        new_scout = Scout(team=team, round=round, alliance=alliance)
        db.session.add(new_scout)
        db.session.commit()
        
    return render_template('scout.html')

@auth.route('/input')
def input():
    return render_template('input.html')

@auth.route('/data')
def data():
    return render_template('data.html')

@auth.route('/auton', methods=['GET', 'POST'])
def auton():
    if request.method == 'POST':
        auton_taxi = request.form.get('auton_taxi')

        auton_upper_in = request.form.get('auton_upper_in')
        auton_upper_missed = request.form.get('auton_upper_missed')
        auton_upper_unreliable = request.form.get('auton_unreliable_upper')

        auton_lower_in = request.form.get('auton_lower_in')
        auton_lower_missed = request.form.get('auton_lower_missed')
        auton_lower_unreliable = request.form.get('auton_lower_unreliable')
    return render_template('auton.html')

@auth.route('/teleop', methods=['GET', 'POST'])
def teleop():
    if request.method == 'POST':
        tele_taxi = request.form.get('tele_taxi')

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

    return render_template('teleop.html')

@auth.route('/results')
def results():
    return render_template('results.html')

@auth.route('/attempt', methods=['GET', 'POST'])
def attempt():
    if request.method == 'POST':
        team = request.form.get('team')
        round = request.form.get('round')
        alliance = request.form.get('alliance')

        # Auton
        taxi = request.form.get('auton_taxi')

        auton_upper_in = request.form.get('auton_upper_in')
        auton_upper_missed = request.form.get('auton_upper_missed')
        auton_upper_unreliable = request.form.get('auton_unreliable_upper')

        auton_lower_in = request.form.get('auton_lower_in')
        auton_lower_missed = request.form.get('auton_lower_missed')
        auton_lower_unreliable = request.form.get('auton_lower_unreliable')

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

        new_scout = Scout(team=team, round=round, alliance=alliance, auton_taxi=taxi, 
                          auton_upper_in=auton_upper_in, auton_upper_missed=auton_upper_missed, 
                          auton_upper_unreliable=auton_upper_unreliable, auton_lower_in=auton_lower_in,
                          auton_lower_missed=auton_lower_missed, auton_lower_unreliable=auton_lower_unreliable, 
                          tele_upper_in=tele_upper_in, tele_upper_missed=tele_upper_missed, tele_upper_unreliable=tele_upper_unreliable,
                          tele_lower_in=tele_lower_in, tele_lower_missed=tele_lower_missed, tele_lower_unreliable=tele_lower_unreliable,
                          hang=hang, win=win, cargo_bonus=cargo_bonus, hangar_bonus=hangar_bonus)
        db.session.add(new_scout)
        db.session.commit()
        
    return render_template('attempt.html')
