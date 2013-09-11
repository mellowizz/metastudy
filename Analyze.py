#!/usr/bin/python2.7

import csv
import codecs
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-a", "--autor", dest="autor",
                  help="suche fuer autor")
parser.add_option("-t", "--titel", dest="titel",
                  help="suche fuer titel")
parser.add_option("-u", "--untertitel", dest="utitel",
                  help="suche fuer untertitel")
parser.add_option("-d", "--dokumentyp", dest="doku",
                  help="suche fuer Dokument Typ")
parser.add_option("-j", "--jahr", dest="jahr",
                  help="suche fuer Jahr")
parser.add_option("-z", "--zeitschrift", dest="zeitschrift",
                  help="suche fuer Zeitschrift")
parser.add_option("-f", "--freitext", dest="frei",
                  help="suche fuer freitext")
parser.add_option("-s", "--schlag", dest="schlag",
                  help="suche fuer schlagwoerter")
parser.add_option("-m", "--medium", dest="medium",
                  help="suche fuer medium")
parser.add_option("-A", "--Alle", action="store_true", dest="alle",
                  help="suche durch alle optionen")

(options, args) = parser.parse_args()


class MyInfo:
    def __init__(self, options):
        #for opts in options:
        #   self.opts = str(opts)
        self.a = options.autor # string
        self.t = options.titel # string
        self.u = options.utitel # string
        self.d = options.doku # string
        self.j = options.jahr # integer
        self.z = options.zeitschrift # string
        self.f = options.frei # string
        self.s = options.schlag # list
        self.m = options.medium # list
        self.A = options.alle # boolean
    
        
count = 0
year =[]
x = MyInfo(options)



with open ('EL.txt', 'rb') as f:
    reader = csv.reader(f, delimiter='\t')
    try:
            for row in reader:
                if x.a in row[0]:
                    count += 1
                    year.append(row[4])
                    for i in row:
                        print i
        except csv.Error, e:
            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
        finally:
            print count
            for y in year:
                print y
            raw_input()
