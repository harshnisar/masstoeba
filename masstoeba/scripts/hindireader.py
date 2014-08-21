import itertools
import sentencesplitter
import utility

with open('parallel corpus/hindi/agro1.Hindi','rb') as f:
    #hincontent = f.read().decode('utf-8')
    hincontent = f.read()
    hincontent = hincontent.decode('utf-8')

with open('parallel corpus/english/agro1.english','rb') as f:
    engcontent = f.read().decode('utf-8')


hinsentences = []
#Unicode codepoint for poorna viraam or the hindi fullstop is u0964

# hinsentences = hincontent.split(u'\u0964')
hinsentences = sentencesplitter.splitter(hincontent,'hin')

# print hinsentences


engsentences = []
engsentences = sentencesplitter.splitter(engcontent,'eng')


# print len(engsentences)

for i in range(0,len(engsentences)):
    try:
        k = engsentences[i].split('\n')
        engsentences[i] = k[0]
        engsentences.insert(i+1,k[1])    

    except:
        pass    


print 'English sentences count ' , len(engsentences)
print 'Hindi sentence count ' ,len(hinsentences)

if len(engsentences) == len(hinsentences):
    print 'Both have the same number of sentences'



mylist = zip(engsentences,hinsentences)
counter = 0
f = open('logger.txt','wb')

avg_diff = 0
avg_diff_score = 0

for s1,s2 in itertools.izip_longest(engsentences,hinsentences):
    counter = counter + 1
    print '------------------------------\n'
    print s1.encode('utf-8')
    print s2.encode('utf-8')
    print '\n'
    results = utility.sentencesimilarity('hin', s2, 'eng', s1)
    print 'The number of words that matches are : ' + str(results[0])
    avg_diff = avg_diff + abs(results[1])
    avg_diff_score = avg_diff_score + results[0]
print 'Average difference in lenght in parallel sentences is ' + str(avg_diff/counter) 
    



