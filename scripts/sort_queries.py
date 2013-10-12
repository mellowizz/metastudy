#!/usr/bin/python2
# -*- coding: utf-8 -*-
import codecs
from pattern.web    import Google, plaintext, sort
#from collections import Counter
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-q", "--query", dest="query",
                  help="txt file with searchwords")
parser.add_option("-f", "--filename", dest="filename",
                  help="specify filename to save data too")
(options, args) = parser.parse_args()

'''
    open schlaglist
'''
f = codecs.open(options.query, encoding='utf-8')
results = sort(terms=[x.strip() for x in f], context = 'Energiewende')

# create weights
for weight, term in results:
    term = term.encode('utf-8')
    with codecs.open(options.filename, "a", "utf-8") as f:
        print ("%5.2f" % (weight * 100) + '%', repr(term))
        try:
            f.write("%5.2f" % (weight * 100))
            f.write(',')
            f.write(term.encode("utf-8"))
            f.write('\n')
        except UnicodeDecodeError as e:
            print e
