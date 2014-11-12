#!/usr/bin/python

import urllib2
import json
import pprint
import sys

pp = pprint.PrettyPrinter(indent=2)

def fetch_and_print(url):
    response = urllib2.urlopen(url)
    s = response.read()
    data = json.loads(s) #take a string and convert to python object
    pp.pprint(data)

fetch_and_print(sys.argv[1]) #fetch any url and run

# terminal
# python fetch.py "http://api.petfinder.com/pet.get?key=e8eae2c8b71e8add084bb51426a90575&format=json&output=full&id=23143932"
