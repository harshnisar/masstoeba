import subprocess






def corpusreader(lang,n,filename):
    #cmd = ["""grep -i --word-regexp "%s" engsent.txt --count -m 1""" %(x)]
    cmd = ["""awk -F'\t' '($2 == "%s") { print $0 }' %s"""%(lang,filename)]
    try:
        sentences = subprocess.check_output(cmd,shell=True,stderr=subprocess.STDOUT)
        print sentences
    
    except:
        
        print 'Error'



lang = 'eng'
filename = 'sentences.csv'

corpusreader(lang,1,filename)


