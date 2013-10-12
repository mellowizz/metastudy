#!/usr/bin/python2
# -*- coding: utf-8 -*-
'''
  txt_analysis.py
    Given a directory of text files and list of query words, find the
    frequency of words in the list. Write the results to a file in
    alphabetical order

TO DO:
  * give filename where words are found
  * filename to save to specified on cmdline
  * combine sort_queries.py with this.
'''

import codecs, os, sys
from collections import Counter
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-q", "--query", dest="query",
                  help="txt file with searchwords")
parser.add_option("-d", "--dirs", dest="dirs",
                  help="specify directory to use")
(options, args) = parser.parse_args()

# Open query list
f = codecs.open(options.query, encoding='utf-8')

#build querylist counter
schlagList = Counter(x.strip() for x in f)
content = u""

def buildDict (filename):
    #print filename
    with codecs.open(filename, encoding='utf-8') as f:
        cnt = Counter()
        for i in f.read().split():
            try:
                content = i
                content = u" ".join(content.replace(u"\xa0", u" ").strip().split())
            except UnicodeDecodeError as e:
                print e, i
            if content in schlagList.elements():
                schlagList[content] += 1
                cnt[content] += 1
        return (filename, cnt) # why not just write to file?


# get list of files to read from cmdline

listOfFiles = [ i for i in os.listdir(sys.argv[1])]

try:
    articleDict = [buildDict(sys.argv[1] + i) for i in listOfFiles]
except:
    print "error", i

with codecs.open("answers.csv", "a", "utf-8") as f:
    for l,m in sorted(schlagList.most_common(20)):
        f.write(l)
        f.write(",")
        f.write(str(m).encode("utf-8"))
        f.write("\n")
    print schlagList.most_common(20)
