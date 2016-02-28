# -*- coding: utf-8 -*-

from flask import render_template, flash, redirect, request, url_for
from masstoeba import app, db
from forms import TextSubmission, PlayGround
from werkzeug.utils import secure_filename
import os
import scripts
from masstoeba import models
from sqlalchemy.sql.expression import func
import random


CROWD_THRESHOLD = 1


ALLOWED_EXTENSIONS = set(['txt', 'pdf'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS



def submit_to_database(sent_dict, lang):
    '''Puts the sentences recieved by the app into lang-specific
    table of the database'''
    for sent in sent_dict:
        u = models.eng_orphanage(id=hash(sent), sentence=sent, score=sent_dict[sent])
        db.session.add(u)
    db.session.commit()


@app.route('/dataprint', methods=['GET','POST'])
def data_printing():
    if request.method == 'GET':
        print models.ROLE_USER
        # print help(models.eng_orphanage.query.)
        sentences = models.eng_orphanage.query.order_by(models.eng_orphanage.score.desc()).limit(10).all()
        # print type(db.session.query(models.eng_orphanage, func.max(models.eng_orphanage.score)).all())
        print type(sentences)
        for sent in sentences:
            print type(sent)

    return '''Oh yeah'''        

@app.route('/orphanage', methods = ['GET', 'POST'])
def orphanage():
    if request.method == 'GET':
        lang = 'eng'
        sentences = models.eng_orphanage.query.order_by(models.eng_orphanage.score.desc()).limit(10).all()
        selected_sent = sentences[random.randint(0,10)]
        return selected_sent.sentence
        

@app.route('/testingsessions', methods = ['GET', 'POST'])
def testing():
    if request.method == 'GET':
        # sentences = models.eng_orphanage.query.get(-9222808175762007000)
        sentences = db.session.query(models.eng_orphanage).get(-587561644022235800)
        if sentences in db.session:
        	print sentences
        	return 'oh yeah2'



@app.route('/submit', methods = ['GET', 'POST'])
def submit():
    form = TextSubmission()
    if form.validate_on_submit():
        flash('Name of Open Text' + form.name.data + 'The text is : ' + form.text.data)
        return redirect('/submit')
    return render_template('submit.html', 
        title = 'Open Text Submission',
        form = form)


@app.route('/playground', methods=['GET','POST'])
def playground():
    form = PlayGround()
    if request.method == 'POST' and form.validate_on_submit():
        print 'IN POST'
        print request.files
        file = request.files['text']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print filename
            text = file.read().decode('ISO-8859-1')
        print type(text)
        max_thresh = form.max_thresh.data
        min_thresh = form.min_thresh.data
        uncommon_thresh = form.uncommon_thresh.data
        weight_iwf= form.weight_iwf.data 
        weight_common=form.weight_common.data
        weight_firstchar=form.weight_firstchar.data
        weight_len=form.weight_len.data
        picked = scripts.masstoeba.sentence_picker(text, 'eng', min_thresh, max_thresh, uncommon_thresh, '\r\n', weight_len=weight_len, weight_iwf=weight_iwf, weight_firstchar=weight_firstchar, weight_common=weight_common)
        # print picked
        return render_template('results.html', results = picked)
        

    else:
        filepath = 'playground.html'
        newfilepath = os.path.join('masstoeba/static/', filepath)
        return render_template('playground.html', form = form)


@app.route('/new', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print request.files
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print filename
            text = file.read().decode('utf-8')
            #send the text to the script.
            # print scripts.masstoeba.sentence_picker(f)
            max_thresh = 12
            min_thresh = 4
            uncommon_thresh = 1
            print os.getcwd()
            print type(text)
            picked = scripts.masstoeba.sentence_picker(text, 'eng', min_thresh, max_thresh, uncommon_thresh, '\r\n')
            print type(picked)
            submit_to_database(picked, 'eng')
    elif request.method == 'GET':
        return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form action="" method='POST' enctype=multipart/form-data>
          <p><input type=file name=file>
             <input type=submit value=Upload>
        </form>
        '''