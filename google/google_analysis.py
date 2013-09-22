#!/usr/bin/python2
# -*- coding: utf-8 -*-
import codecs, os, sys
from collections import Counter
from optparse import OptionParser
from pattern.web import Google


parser = OptionParser()
parser.add_option("-q", "--query", dest="query",
                  help="txt file with searchwords")
parser.add_option("-d", "--dirs", dest="dirs",
                  help="specify directory to use")
(options, args) = parser.parse_args()
f = codecs.open(options.query, encoding='utf-8')
schlagList = Counter(x.strip() for x in f)
content = u""

def buildDict (resultString, resultUrl, resultDate):
    with codecs.open("output.txt", "a", "utf-8") as r:
        r.write(resultDate)
        r.write(",")
        r.write(resultString)
        r.write("\n")
    cnt = Counter()
    for i in resultString.split():
        try:
            content = i
            content = u" ".join(content.replace(u"\xa0", u" ").strip().split())
        except UnicodeDecodeError as e:
            print e, i
        if content in schlagList.elements():
            schlagList[content] += 1
            cnt[content] += 1
    return (resultDate, resultUrl, cnt) # why not just write to file?


engine = Google(license=None, language='de') #'0001401664590345725200:dx8-iwqnvyw')

for result in engine.search('Energiewende'):
    articleDict = [buildDict(unicode(result.text), result.url, result.date)]



with codecs.open("google.csv", "a", "utf-8") as f:
    for l,m in sorted(schlagList.most_common(20)):
        f.write(l)
        f.write(",")
        f.write(str(m).encode("utf-8"))
        f.write("\n")
    print schlagList.most_common(20)

'''
with codecs.open("google2.csv", "a", "utf-8") as f:
    for x,y,z in articleDict:
        f.write(x)
        f.write(",")
        f.write(str(y).encode("utf-8"))
        f.write(",")
        f.write(z)
        f.write("\n")
'''
