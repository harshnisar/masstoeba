
from flask import Flask
import nltk
from masstoeba import sentence_picker
import operator
import sentencesplitter



app = Flask(__name__)

import logging
from logging import StreamHandler
file_handler = StreamHandler()
app.logger.setLevel(logging.DEBUG)  # set the desired logging level here
app.logger.addHandler(file_handler)



@app.route('/')
def hello():
    STOPWORDS = nltk.corpus.stopwords.words('english')
    with open('requirements.txt') as f:
        content = f.read()
    print 'helli'
    return 'Hello Worldhh!' + content


@app.route('/masstoeba/')
def mass():
    app.logger.debug('A value for debugging')
    app.logger.warning('A value for warning')
    min_thresh = 4
    max_thresh = 12
    uncommon_thresh = 1
    with open('kafka.txt', 'rb') as f:
        text = f.read().decode('utf-8')


    lines = sentencesplitter.splitter(text, 'eng')
    print 'in here'

    picked = sentence_picker(min_thresh, max_thresh, uncommon_thresh, lines, '\r\n')
    sorted_picked = sorted(picked.iteritems(), key=operator.itemgetter(1))
    return str(sorted_picked)

    #Will have to return dictionary of sentences? Or named tuples


if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)

