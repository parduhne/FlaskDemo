import os

import string
import nltk.corpus
import cmudict
from flask import Flask, request, redirect, render_template, session, url_for, g

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY='devIAm')  # Needed for session tracking
  # Note flask does CLIENT session data storage!  Watch data sizes!


@app.route('/', methods=['GET','POST'])
def calculate():
  t = {'a': 0, 'b': 0, 'c': 0}
  if request.method == 'POST':
    t['a'] = request.form['a']
    t['b'] = request.form['b']
  elif 'a' in request.args:
    t['a'] = request.args.get('a')
    t['b'] = request.args.get('b')
  t['c'] = int(t['a']) * int(t['b'])
  # Update the number of visits
  # session is a dict which persists.  Stored in client cookie (no local storage)
  if 'times' not in session:
    session['times'] = 0
  session['times'] += 1

  return render_template('index.html', t = t, times = session['times']) # Send t to the template

@app.route('/logout')
def logout():
  session.clear()
  return redirect(url_for('calculate'))  # Calculate is the fn name above!


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Enable on all devices so Docker works!
