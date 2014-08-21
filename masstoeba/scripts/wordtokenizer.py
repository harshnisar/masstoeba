''' Has methods useful for tokenizing words
'''

import string
import csv
import nltk
import re
import utility
from nltk.tokenize import WhitespaceTokenizer
# with open('parallel corpus/hindi/agro1.Hindi','rb') as f:
#     lines = f.read()
#     lines = lines.decode('utf-8')

# with open('parallel corpus/english/agro1.english','rb') as f:
#     lines = f.read()
#     lines = lines.decode('utf-8')





def wordtokenizer(lang, text):
    '''Takes lang and text, returns list of words in lowercase from, strips of the
     punctuation'''
    if lang == 'eng':
        words = WhitespaceTokenizer().tokenize(text)
        clean_words = []
        # clean_words = [word.strip(string.punctuation) for word in words]
        for word in words:
            t_word = word.strip(string.punctuation)
            if t_word:
                clean_words.append(t_word.lower())
        return clean_words

    else:
        stopchar = utility.get_lang_info('hin')[3][0]
        text = text.replace(',', ' ')
        words = text.split()
        return [word.strip(string.punctuation+stopchar) for word in words]

# words = wordtokenizer('eng',lines)

# for word in words:
#     print word.encode('utf-8')

