#!/usr/bin/python

import sys
import csv
import pprint
from numpy import arange, array, sum
from collections import defaultdict

def main():
  #csv filename to evaluate => first argument in command prompt
  filename = '../data/' + sys.argv[1]
  
  with open (filename) as csvfile:
    a = array([row.strip().split(',') for row in csvfile])
    lengthRow = len(a[0])
    coldict = dict((a[0,col],a[1:,col]) for col in arange(0,lengthRow-1))
    ###check the length issue
  
  print coldict

  #calculate the number of correct answers
  corrResp = coldict['key_resp.corr']
  sumcorr = sum([map(int, i) for i in corrResp])
  print 'number of correct responses: ' + str(sumcorr)

  #calculate the frequency of BA, WA responses
  d = defaultdict(int)
  for ans in coldict['key_resp.keys']:
    d[ans] += 1

  #gets the number of BA, WA responses
  numBA = d['1']
  numWA = d['2']

  #find the number of BAs, WAs correct
  corrKey = coldict['correct']
  keyResp = coldict['key_resp.keys']
  baCorr, baErr, waCorr, waErr, noneErr, noiseErr = 0, 0, 0, 0, 0, 0
  for i in arange(0,len(coldict[0])):
    if corrKey(i) == keyResp(i):
      if corrKey(i) == 1:
        baCorr += 1
      if corrKey(i) == 2:
	      waCorr += 1
    else #must do a fix for if the response is 'None'
      if corrKey(i) == 1:
        baErr += 1
      if corrKey(i) == 2:
        waErr += 1

      if keyResp(i) == 'None':
        noneErr += 1
      if keyResp(i) == 3:
        noiseErr += 1

  with open codey.csv as codeycsv:
    codeyfile = array([row.strip().split(',') for row in codeycsv])
    codey = a[0:,1] #take codey column instead of index column
  
  #baCorr (number of BAs correct)
  #waCorr (number of WAs correct)

  #test on the total number of correct answers
  if baCorr + waCorr == sumcorr:
    print 'total correct test: passed'
  else
    print 'total correct test: failed'

  #test on number of error responses
  if sumcorr + noneErr + noiseErr == len(corrKey):
    print 'total error test: passed'
  else
    print 'total error test: failed'
  
  
  print 'number times answered BA: ' + str(numBA)
  print 'number times answered WA: ' + str(numWA)

if __name__ == '__main__':
  main()

