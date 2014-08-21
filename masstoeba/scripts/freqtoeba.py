import nltk
import corpusreader
import wordtokenizer
import pickle



def less_stopwords(wordlist, stopwordset):
    # print stopwordset
    # for word in stopwordset:
    #     print word.encode('utf-8')
    # print 'a' in stopwordset
    '''Accepts a list of words and returns a list without any stopwords'''
    if stopwordset:
        return list(set(wordlist) - stopwordset)
    else:
        return wordlist    

def file_generator(filename):
    with open(filename, 'rb') as fil:
        lines = fil.readlines()
        for line in lines:
            yield line

def load_set_stopwords(filename):
    stopwordset = set()
    gen = file_generator(filename)
    for line in gen:
        # print line
        stopwordset.add(line.rstrip('\r\n ').decode('utf-8'))
    # print stopwordset
    return stopwordset

def fdist_gen(lang, corpusfile, stopwordfile=False):
    '''Returns the frequency distribution (nltk.probability.FreqDist)
    of a language based on the exisiting
    Tatoeba corpus. If stopwordfile set to true, removes the stop words from
    the frequency distrubution based on the stopword list provided to the
    function.
    '''

    sentences = corpusreader.corpusreader(lang, corpusfile)

    fdist = nltk.FreqDist()
    # STOPWORDS = set(nltk.corpus.stopwords.words('english'))
    if stopwordfile:
        stopwordset = load_set_stopwords(stopwordfile)
    else:
        stopwordset = False    
    for sentence in sentences:
        words = wordtokenizer.wordtokenizer('hin', sentence)
        # print len(words)
        words = less_stopwords(words, stopwordset)
        # print len(words)
        # print '\n'
        # print words
        for word in words:
            
            fdist.inc(word.lower())

    # for key in fdist.keys()[:50]:
        # print key.encode('utf-8'), fdist[key]

    # print fdist['football']
    # print fdist['soccer']
    # print fdist['tom']


    # fdist.plot(500)
    print type(fdist)
    return fdist

def fdist_loader(lang):
    ''' Loads a pre-made pkl file which contains the frequency distribution in
    a particular language. Returns -1 if the pickle doesnt exist
    '''  
    try:
        with open('fdists/fdist_%s.pkl'%(lang)) as f:
            fdist = pickle.load(f)
            print 'loading pickle file'
            return fdist
    except:
        return -1

# stopwordfile = 'stopword/stop-words_english_1_en.txt'
#1 stopwordset = load_set_stopwords(stopwordfile)   
# fdist = fdist_gen('eng', 'sentences.csv', 'stopword/stop-words_english_1_en.txt')
# fdist = fdist_gen('eng', 'sentences.csv')
# fdist = fdist_gen('hin', 'sentences.csv', 'stopword/stop-words_hindi_1_hi.txt')
# topwords('hin', 'sentences.csv', 'hindi_sw.txt')

def iwf(word, fdist):
    '''Takes word and fdist, and returns the word frequency. Return 0 if none'''
    
    return fdist[word]
    


# while True:
#     k = raw_input('word')
#     print iwf(k, fdist)

