import subprocess
import traceback,sys,os

my_env = os.environ
my_env['PYTHONIOENCODING'] = 'utf-8'

def corpusreader(lang,filename,n = 0):
    #TODO: To be replaced with csv or pure python
    #cmd = ["""grep -i --word-regexp "%s" engsent.txt --count -m 1""" %(x)]
    cmd = ["""awk -F'\t' '($2 == "%s") { print $0 }' %s"""%(lang,filename)]
    try:
        sentenceblock = subprocess.check_output(cmd,shell=True,stderr=subprocess.STDOUT).decode('utf-8')
        # print type(sentenceblock)
        sentences = []
        sentences = sentenceblock.split('\n')

        for i in range(0,len(sentences)-1):

            sentences[i]=sentences[i].split('\t')[2]
    except:
        traceback.print_exc(file=sys.stdout)
        
        return 0

    if n==0:
        return sentences
    else:
        return sentences[0:n]




if __name__ == '__main__':
    #TODO : Explore getopt, to get the arguments, if we really want this to be run through the command line. I did command line only for testing purposes
    arguments = sys.argv
    # print repr(corpusreader(arguments[1], arguments[2], int(arguments[3]))).decode("unicode-escape")
    for sentence in corpusreader(arguments[1], arguments[2], int(arguments[3])):
        print sentence.encode('utf-8')