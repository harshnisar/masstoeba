import subprocess
#f = open('en.txt','rb')
f = open('wikifiction.txt','rb')

data = f.readlines()


arg = 'wiki'

wordnot = []
cnt = 0
for line in data:
    cnt = cnt + 1
    if arg == 'f':
        x,y = line.split()
    elif arg == 'wiki':
        x = line.split()
        x = x[0]
    print x
    
    cmd = ["""grep -i --word-regexp "%s" engsent.txt --count -m 1""" %(x)]
    try:
        count = subprocess.check_output(cmd,shell=True,stderr=subprocess.STDOUT)
        print int(count)
        count = int(count)
        #print type(count)
        if count == 0:
            wordnot.append(x)
    
    
    except:
        wordnot.append(x)
        print wordnot

    if cnt == 2000:
        break
print wordnot
print len(wordnot)
print len(wordnot)/20