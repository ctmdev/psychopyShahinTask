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

  with open ('codey.csv') as codeycsv:
    codeyfile = array([row.strip().split(',') for row in codeycsv])
    codey = codeyfile[0:,1] #take codey column instead of index column

  #instantiate important data columns
  isCorrect = coldict['key_resp.corr']
  keyResp = coldict['key_resp.keys']

  #create list of data tuples for each trial
  trials = [None]*len(keyResp)
  for i in arange(0,len(keyResp)):  
    trials[i] = (codey[i],isCorrect[i],keyResp[i])

  #evaluate trial tuples
  cod1, cod2, cod3, cod4, cod5, cod6, cod7, cod8, cod9 = 0,0,0,0,0,0,0,0,0
  for dt in trials:
    cod1 = cod1 + corrCod1(dt)
    cod2 = cod2 + corrCod2(dt)
    cod3 = cod3 + corrCod3(dt)
    cod4 = cod4 + corrCod4(dt)
    cod5 = cod5 + corrCod5(dt)
    cod6 = cod6 + corrCod6(dt)
    cod7 = cod7 + corrCod7(dt)
    cod8 = cod8 + corrCod8(dt)
    cod9 = cod9 + corrCod9(dt)

  baTot = cod1 + cod2 + cod3 + cod4 + cod5 + cod6
  waTot = cod7 + cod8 + cod9
  synTot = cod1 + cod4 + cod7
  maleTot = cod3 + cod6 + cod9
  femaleTot = cod2 + cod5 + cod8
  bawaTot = cod4 + cod5 + cod6
  nosynTot = cod5 + cod6
  bawaMaleTot = cod6
  bawaFemaleTot = cod5

  print 'Ba Correct: ' + str(baTot)
  print 'Wa Correct: ' + str(waTot)
  print 'Synthetic Correct: ' + str(synTot)
  print 'Male Correct: ' + str(maleTot)
  print 'Female Correct: ' + str(femaleTot)
  print 'BaWa Correct: ' + str(bawaTot)
  print 'Non-Synthetic Correct: ' + str(nosynTot)
  print 'BaWa Male Correct: ' + str(bawaMaleTot)
  print 'BaWa Female Correct: ' + str(bawaFemaleTot)
    
#functions to return 1 if codey type value is true
def corrCod1(datatuple):
  return 1 if datatuple[0] == '1' and datatuple[1] == '1' else 0

def corrCod2(datatuple):
  return 1 if datatuple[0] == '2' and datatuple[1] == '1' else 0

def corrCod3(datatuple):
  return 1 if datatuple[0] == '3' and datatuple[1] == '1' else 0

def corrCod4(datatuple):
  return 1 if datatuple[0] == '4' and datatuple[1] == '1' else 0

def corrCod5(datatuple):
  return 1 if datatuple[0] == '5' and datatuple[1] == '1' else 0

def corrCod6(datatuple):
  return 1 if datatuple[0] == '6' and datatuple[1] == '1' else 0

def corrCod7(datatuple):
  return 1 if datatuple[0] == '7' and datatuple[1] == '1' else 0

def corrCod8(datatuple):
  return 1 if datatuple[0] == '8' and datatuple[1] == '1' else 0

def corrCod9(datatuple):
  return 1 if datatuple[0] == '9' and datatuple[1] == '1' else 0

if __name__ == '__main__':
  main()

