#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import codecs, sys
from pdfminer.pdfparser import PDFParser, PDFDocument

txtfile = "schlag.txt"

f = codecs.open(txtfile, encoding='utf-8')

schlaglist = [x.split('\n') for x in f] # list

'''
for x in schlaglist:
    print u(x)
'''
try:
    fp = open('/home/niklasmoran/EL/skript211.pdf')
    print (fp.type())
    parser = PDFParser(fp)
    doc = PDFDocument()
    parser.set_document(doc)
    doc.initialize('')

    outlines = doc.get_outlines()
    print outlines.type() 
except:
    print "that didn't work", sys.exc_info()[0]
