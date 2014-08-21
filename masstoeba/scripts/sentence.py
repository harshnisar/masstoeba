import nltk

eng = open('two bullocks','rb')
print type(eng)
count = 0

sentences = []
text_eng = eng.read()

sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
sentences = (sent_detector.tokenize(text_eng.strip()))

for sentence in sentences:
    print sentence
    print 'LALA'
    count = count + 1

print count

eng.close()