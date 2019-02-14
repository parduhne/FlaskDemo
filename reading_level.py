# Test program for lab 1
# Use mary had a little lamb as source
# 5.25w/s
# 1.47s/w
# calculated reading age = 3.8
import os
import string
import nltk.corpus
import cmudict
from flask import Flask, request, redirect, render_template, session, url_for, g, jsonify
#from nltk.cmudict import cmudict
d = cmudict.dict()

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY='devIAm')

def words_per_sentence(text):
    text = text.split('.')
    count = 0
    sum = 0
    for x in text:
        x = x.split()
        if (len(x) > 0):
            sum += len(x)
            count += 1
    return sum/count

def avg_syllable_per_word(text):
    text = text.split()
    syl = []
    for word in text:
        sylword = nsyl(word)
        if sylword is not None:
            for x in sylword:
                syl.append(x)

    if(len(syl) <= 0):
        return 0
    num = sum(syl)
    return num/len(syl)

def nsyl(word):
  return [len(list(y for y in x if y[-1].isdigit())) for x in d[word.lower()]]

@app.route('/', methods=['GET'])
def calculateAge():
    #file = open("words.txt", "r")
    t = {'text': "", 'age': 0,}
    if 'text' in request.args:
        fileArr = request.args.get('text')
        #file.close()
        wpers = words_per_sentence(fileArr)
        sperw = avg_syllable_per_word(fileArr)
        FKRA = (0.39 * wpers) + (11.8 * sperw) - 15.59
        t['age'] = FKRA
    if 'json' in request.args:
        return jsonify(t['age'])
    if 'times' not in session:
      session['times'] = 0
    session['times'] += 1

    return render_template('index.html', t = t, times = session['times'])

@app.route('/logout')
def logout():
  session.clear()
  return redirect(url_for('calculateAge'))  # Calculate is the fn name above!

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
