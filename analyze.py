#!/usr/bin/python2.7

import csv, sys, collections
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
    def __init__(self, autor, titel, utitel, doku, jahr, zeitschrift, frei, schlag):
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

class Doku:
    def __init__(self, autor, titel, utitel, doku, jahr, zeitschrift, frei, schlag):
        self.a = autor # string
        self.t = titel # string
        self.u = utitel # string
        self.d = doku # string
        self.j = jahr # integer
        self.z = zeitschrift # string
        self.f = frei # string
        self.s = [x.strip() for x in schlag.split(';')] # list
    def get(self):
        return (self.a, self.t, self.u, self.d, self.j, self.z, self.f, self.s)

with open ('EL.csv', 'rb') as f:
        reader = csv.DictReader(f, delimiter=",", quotechar='"')
        fieldnames = [i for i in reader.fieldnames]
        read = csv.reader(f, delimiter=",", quotechar='"')
        searchlist = []
        authorlist = []
        try:
            #articles = dict[Doku(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]) for row in read]
            for i in read:
                print i[0]
                authorlist.append(i[0])
            print collections.Counter(authorlist).most_common(10)
            #print articles[1].a
        except csv.Error, e:
            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
        except KeyError, b:
            sys.exit('key not found: %s' % b.message)
