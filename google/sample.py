#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import httplib2
import pprint
import sys

from apiclient import discovery
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-y", "--year", dest="year",
                  help="give year")
parser.add_option("-q", "--query", dest="query",
                  help="give a query string")

(options, args) = parser.parse_args()

def convertYears(y):
    if y is '2013':
        return 1
    elif "-" in y:
        y1, y2 = y.split('-')
        return int(y2) - int(y1)
    else:
        return 2013 - int(y)

def main(argv):
  # Create an httplib2.Http object to handle our HTTP requests .
  http = httplib2.Http()

  # Construct the service object for the interacting with the CustomSearch API.
  service = discovery.build('customsearch', 'v1',  developerKey='AIzaSyBRLjvH-_YmbcBN-fDvEHdmIqyErQHNH8w', http=http)
  timeFrame = convertYears(options.year) 
  res = service.cse().list(
    q=options.query,
    cx='001401664590345725200:dx8-iwqnvyw',
    lr='lang_de',
    dateRestrict=timeFrame,#"y:r:".join(options.year),
    ).execute()
  print res["queries"]



if __name__ == '__main__':
  main(sys.argv)
