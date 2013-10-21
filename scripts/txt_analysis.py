#!/usr/bin/python2
# -*- coding: utf-8 -*-
'''
  txt_analysis.py
    Given a directory of text files and list of query words, find the
    frequency of words in the list. Write the results to a file in
    alphabetical order.
    One can also specify number of most common words and a filename
    to save to.

TO DO:
  * put everything in main
  * give filename where words are found
  * combine sort_queries.py with this.
  * speed improvements
  * error handling
'''

import codecs, os, sys
from collections import Counter
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-q", "--query", dest="query",
                  help="txt file with searchwords")
parser.add_option("-d", "--dirs", dest="dirs",
                  help="specify directory to use")
parser.add_option("-n", "--num", dest="nums",
                  help="specify how many of the most common words should be printed") # default is 20
parser.add_option("-f", "--filename", dest="fname",
                  help="specify filename") # default is results.csv
(options, args) = parser.parse_args()

def buildDict (filename):
    #print filename
    with codecs.open(filename, encoding='utf-8') as f:
        cnt = Counter()
        for content in f.read().split():
            try:
                # sanitize content = i
                content = u" ".join(content.replace(u"\xa0", u" ").strip().split())
            except UnicodeDecodeError as e:
                print e, i
            if content in schlagList.elements():
                schlagList[content] += 1
                cnt[content] += 1
        return (filename, cnt) # why not just write to file?

# write to file
def writeResults (filename, n):
    with codecs.open(filename, "a", "utf-8") as f:
        for l,m in sorted(schlagList.most_common(20)):
            f.write(l)
            f.write(",")
            f.write(str(m).encode("utf-8"))
            f.write("\n")
            #print schlagList.most_common(20)


# Open query list
f = codecs.open(options.query, encoding='utf-8')
#build querylist counter
schlagList = Counter(x.strip() for x in f)
content = u""
# get list of files to read from cmdline
listOfFiles = [ i for i in os.listdir(options.dirs)]
try:
    articleDict = [buildDict(options.dirs + i) for i in listOfFiles]
except:
    print "error", i

# write the results
writeResults(options.fname, options.nums)
