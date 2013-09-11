#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
    @Author Niklas Moran niklas@niklasmoran.com
    Program takes in a directory full of pdfs and searches for the top twenty
    To do:
        take number to pass to cnt
        take path to schlagworter list
        write out data in CSV
        add title
    Note:
        might be faster just to save all as txt

'''

import codecs, sys, os, time
from collections import Counter
from pyPdf import PdfFileWriter, PdfFileReader

# -- Get Keywords to search for --- #
txtfile = "schlag.txt"
f = codecs.open(txtfile, encoding='utf-8')
schlaglist = [x.strip().lower() for x in f]

cnt = Counter()
# returns a string containg all the text in the pdf
def getPDFContents(path):
    # print % (input1.getDocumentInfo().title)
    try:
        content = ""
        pdf = PdfFileReader(file(path, "rb")) 
        # get all pages and put them in a string
        if pdf.isEncrypted:
            print "%s is encrypted!" % path 
            pass
        else:
            for i in range(0, pdf.getNumPages()):
                #i = pdf.getPage(i).extractText().lower()
                #for word in i:
                #    if word in schlaglist:
                #        cnt[word] +=1
                #        
                content += pdf.getPage(i).extractText().lower() + " \n"
            content = u" ".join(content.replace(u"\xa0", u" ").strip().split())
    except ValueError as d:
        print d.args
        pass
    except Exception as e:
        print e.args
        pass
    return content

theList = []
append = theList.append
t = time.time()
for i in os.listdir(sys.argv[1]):
    append(getPDFContents(sys.argv[1] + i))

for i in theList:
        for word in i.split():
            if word in schlaglist:
                cnt[word] += 1

print cnt.most_common(20)
print "%.3f" % (time.time() - t)
