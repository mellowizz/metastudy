#!/usr/bin/python2
# -*- coding: utf-8 -*-
import codecs, os, sys
from collections import Counter
from optparse import OptionParser
from pattern.web import Google

engine = Google(license=None, language='de') #'001401664590345725200:dx8-iwqnvyw', language='de')

for result in engine.search('Energiewende', cached=False):
    print repr(result.text)
