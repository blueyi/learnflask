# -*- coding: utf-8 -*-

import random
from flask import Flask, render_template, flash, redirect, url_for, session
from flask_wtf import Form
from wtforms import IntegerField, SubmitField
from wtforms.validators import Required, NumberRange
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Very Long String'
app.config['BOOTSTRAP_SERVER_LOCAL'] = True
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    session['number'] = random.randint(0, 1000)
    session['times'] = 10
    return render_template('index.html')

@app.route('/guess', methods=['GET', 'POST'])
def guess():
   times = session['times']
   result = session.get('number')
   form = GuessNumberForm()
   if form.validate_on_submit():
       times -= 1
       session['times'] = times
       if times == 0:
           flash('You have lost!', 'danger')
           return redirect(url_for('.index'))
       answer = form.number.data
       if answer > result:
           flash('Too big! Only %s chances left!' %times, 'warning')
       elif answer < result:
           flash('Too small! Only %s chances left!' %times, 'info')
       else:
           flash('You Win!',  'success')
           return redirect(url_for('.index'))
   return render_template('guess.html', form=form)


class GuessNumberForm(Form):
    number = IntegerField(u'Input an integer number(0~1000)',
                          validators=[Required('Please input a validate number'),
                                      NumberRange(0, 1000, 'Please input in 0~1000!')])
    submit = SubmitField('Submit')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
