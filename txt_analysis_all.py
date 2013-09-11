#!/usr/bin/python2
# -*- coding: utf-8 -*-
import codecs, os, sys
#import nltk
#from nltk import FreqDist
from collections import Counter

txtfile = "schlag.txt"
f = codecs.open(txtfile, encoding='utf-8')
#schlaglist = 
bigCnt = Counter([x.strip() for x in f])
content = u""
def buildDict (filename):
    #print filename
    with codecs.open(filename, encoding='utf-8') as f: # 'rb') as f:
        cnt = Counter()
        for i in f.read().split():
            try:
                content = i
                content = u" ".join(content.replace(u"\xa0", u" ").strip().split())
            except UnicodeDecodeError as e:
                print e, i
            if content in list(bigCnt.elements()):
                bigCnt[content] += 1
                cnt[content] += 1
        return (filename, cnt) # why not just write to file?


# get list of files to read from cmdline
listOfFiles = [ i for i in os.listdir(sys.argv[1])]

# build a dictionary of
try:
    articleDict = [buildDict(sys.argv[1] + i) for i in listOfFiles]
except:
    print "error", i

print bigCnt.most_common(20)
with codecs.open("answers.csv", "w", "utf-8") as f:
    for word,num in sorted(bigCnt.most_common(20)):
        f.write(word)
        f.write(",")
        f.write(str(num).encode("utf-8"))
        f.write("\n")
'''
for x,y in articleDict:
        f.write(x)
        f.write(y.most_common(10)])
        f.write("\n")
'''
