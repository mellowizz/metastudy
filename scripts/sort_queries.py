#!/usr/bin/python2
# -*- coding: utf-8 -*-
'''
  sort_queries.py
    Takes a list of words to search for as .txt specified by -q
    and outputs to a file specified by -f. Prints comma separated
    ranking of the search term in google in context of "Energiewende".

TO DO:
  * specify context on cmd line or in the query file
  * get the total count and include it.
  * other stuff
'''

import codecs
from pattern.web    import Google, plaintext, sort
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-q", "--query", dest="query",
                  help="txt file with searchwords")
parser.add_option("-f", "--filename", dest="filename",
                  help="specify filename to save data too")
(options, args) = parser.parse_args()

# open the list of query words
f = codecs.open(options.query, encoding='utf-8')

# build results in context of the "Energiewende"
results = sort(terms=[x.strip() for x in f], context = 'Energiewende')

# create weights
for weight, term in results:
    term = term.encode('utf-8')
    with codecs.open(options.filename, "a", "utf-8") as f:
        print ("%5.2f" % (weight * 100) + '%', repr(term))
        try:
            f.write(term.encode("utf-8"))
            f.write(',')
            f.write("%5.2f" % (weight * 100))
            f.write('\n')
        except UnicodeDecodeError as e:
            print e
