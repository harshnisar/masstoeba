'''Uses frequency distribution of a given language to generate a list
of stopwords based on clustering.'''

import freqtoeba
from utility import file_generator
import nltk
# from pylab import *
import pylab
import pickle
from numpy import mean

def load_set_stopwords(filename):
    stopwordset = set()
    gen = file_generator(filename)
    for line in gen:
        # print line
        stopwordset.add(line.rstrip('\r\n ').decode('utf-8'))
    # print stopwordset
    return stopwordset

def stopwordgen():
    try:
        with open('fdist.pkl') as f:
            fdist = pickle.load(f)
            print 'loading'
    except:
        fdist = freqtoeba.fdist_gen('eng', 'sentences.csv')
        with open('fdist.pkl','w') as f:
            pickle.dump(fdist, f)

    # fdist = freqtoeba.fdist_gen('hin', 'sentences.csv')
    x = fdist.values()
    maximum = fdist[fdist.max()]
    y = [50 for item in x]
    pylab.plot(x, y, 'm.', label='sampled')
    stopwords = list(load_set_stopwords('stopword/stop-words_english_1_en.txt'))
    
    STOPWORDS = list(set(nltk.corpus.stopwords.words('english')))
    totstopwords = len(STOPWORDS)
    for word in STOPWORDS:
        pylab.plot([fdist[word.lower()]], [45], 'r.')
        # print word, fdist[word.lower()]
    xstop = []
    ystop = []
    stopwordenc = 0
    xnor = []
    ynor = []
    norenc = 0
    norperc = 0
    for word in fdist:
        
        # word = fdist[sample]
        # print word
        if word in STOPWORDS:
            stopwordenc += 1
            # stopwordperc = (float(totstopwords - stopwordenc)/totstopwords)*100
            stopwordperc = (float(stopwordenc)/totstopwords)*100
            xstop.append(fdist[word.lower()])
            ystop.append(stopwordperc)
        else:
            norenc += 1
            norperc = (float(norenc)/len(fdist))*100
            xnor.append(fdist[word])
            ynor.append(norperc)

    pylab.plot(xstop, ystop, linestyle='-', color='c')
    # pylab.plot(xnor, ynor, linestyle='--', color='b')
    pylab.grid(True)
    # print xnor
    # print ynor
    # print x
    # print mean(x)

    #plotting the number of words against frequency
    scores = {}
    wordloss = 0
    for word in fdist:
        try:
            scores[fdist[word]] = scores[fdist[word]] + 1
        except:
            scores[fdist[word]] =  1
        if fdist[word] > 3540 and word not in STOPWORDS:
            wordloss =  wordloss + 1


    pylab.plot(scores.keys(), scores.values(), linestyle = '-', color = 'b')
    print 'word loss is  ', wordloss

    # print scores
    print len(STOPWORDS)

    #end of that part
    pylab.ylim(-2, 110)
    pylab.xlim(-2000, maximum)
    pylab.xlabel('Frequency')
    pylab.ylabel('Percentage of stopwords above threshold')
    pylab.title('Stopwords and Frequencies Experiment')
    pylab.show()

stopwordgen()

# STOPWORDS = list(set(nltk.corpus.stopwords.words('english')))
# for word in STOPWORDS:
#     print word