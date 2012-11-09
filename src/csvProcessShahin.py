#!/usr/bin/python

import sys
import csv
import pprint
from numpy import arange, array, sum
from collections import defaultdict

def main():
  #csv filename to evaluate => first argument in command prompt
  filename = sys.argv[1]
  
  with open (filename) as csvfile:
    a = array([row.strip().split(',') for row in csvfile])
    lengthRow = len(a[0])
    coldict = dict((a[0,col],a[1:,col]) for col in arange(0,lengthRow-1))
    ###check the length issue
  
  print coldict

  #calculate the number of correct answers
  numcorr = coldict['enterResp.corr']
  sumcorr = sum([map(int, i) for i in numcorr])
  print 'number of correct responses: ' + str(sumcorr)

  #calculate the frequency of responses
  d = defaultdict(int)
  for ans in coldict['enterResp.keys']:
    d[ans] += 1
  print 'number times answered BA: ' + str(d['1'])
  print 'number times answered WA: ' + str(d['2'])

if __name__ == '__main__':
  main()

