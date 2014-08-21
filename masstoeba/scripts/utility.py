 # coding: utf-8
''' Contains simple Utilities which will be helpful throughout masstoeba
'''


import wordtokenizer
import csv
import nltk
from collections import namedtuple


STOPWORDS = set(nltk.corpus.stopwords.words('english'))

def less_stopwords(wordlist):
    '''Accepts a list of words and returns a list without any stopwords'''

    #Remember, stop words are not in unicode for other languages, make sure about this.
    return list(set(wordlist) - STOPWORDS)

def unwrapper(line, newline_char):
    '''Used on a sentence which have been extracted from wrapped
    texts, and hence contain multiple newline characters inside it
    . Takes a string and returns without newline characters.
    Replaces newline_char with space.
    '''

    line = line.encode('utf-8').replace(newline_char, ' ')
    line = line.strip()
    return line.decode('utf-8')


def csv_generator(filename, delim):
    with open(filename, 'rb') as f:
        rows = csv.reader(f, delimiter=delim)
        for row in rows:
            yield row

def file_generator(filename):
    with open(filename, 'rb') as fil:
        lines = fil.readlines()
        for line in lines:
            yield line


def translation_lookup(word):
    '''For now looks up translation from hin to english from the en_hi file
     from wiktionary'''
    csvgen = csv_generator('en_hi.csv', '\t')
    for row in csvgen:
        # print word, ' checking against ', row[1].decode('utf-8')
        if word == row[1].decode('utf-8'):
            return row[0].decode('utf-8')
    return False


def get_lang_info(lang):
    '''Reads langinfo.csv and returns information about the particular language as a namedtuple

    Returns in order : codename, language, need_punkt, stopcharlist(unicode)
    '''
    langinfolist = []
    Lang  = namedtuple('Lang',['codename','language', 'need_punkt','stopchar'])
    with open("langinfo.csv",'rb') as f:
        c = csv.reader(f,delimiter = '\t')
        for row in c:
            # print row
            if row[0] == lang:
                langinfolist = row
                break


    return     Lang(lang, langinfolist[1].decode('utf-8'), langinfolist[2]=='True', langinfolist[3].decode('utf-8').split(u','))        



def sentencesimilarity(lang1, sentence1, lang2, sentence2):
    '''Lang1 will be converted to lang2 and then similarity between the newly
     translated sentece and lang2 willbe calculated
       We try to keep lang2 as english

    '''
    print 'First sentence bag got is : '
    sentence1_words = wordtokenizer.wordtokenizer(lang1,sentence1.lower())
    test = []
    for word in sentence1_words:
        print word.encode('utf-8') + ',',
    len_sent_one = len(sentence1_words)
    


    print '\nSecond sentence bag got is : '
    sentence2_words = wordtokenizer.wordtokenizer(lang2,sentence2.lower())
    print sentence2_words

    len_sent_two = len(sentence2_words)
    len_differece = len_sent_one - len_sent_two
    print 'Difference in sentence lenghts is %s - %s = %s' %(len_sent_one, len_sent_two, len_differece)

    # return '1'
    translated_sentence = []
    for word in sentence1_words:
        translated_word = translation_lookup(word)
        #print translated_word
        if translated_word:
            translated_sentence.extend(translated_word.split())

    print 'Translated bag for sentence1 is : '
    print translated_sentence

    #Now we have translated sentence in bag of words format. We need to check how many of these words exist in sentence2
    same_word_count = 0
    for word in translated_sentence:
        if word in sentence2_words:
            print word
            same_word_count = same_word_count + 1

    return [same_word_count,len_differece]


# w = 'गुरु'.decode('utf-8')

# print translation_lookup(w)

testsen1 = 'how much girl life'.decode('utf-8')
testsen2 = 'कितना लड़की जी'.decode('utf-8')

# print testsen1.encode('utf-8')
# print testsen2.encode('utf-8')

# print sentencesimilarity('hin',testsen2,'eng',testsen1)