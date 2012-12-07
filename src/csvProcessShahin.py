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
  numcorr = coldict['key_resp.corr']
  sumcorr = sum([map(int, i) for i in numcorr])
  print 'number of correct responses: ' + str(sumcorr)

  #calculate the frequency of responses
  d = defaultdict(int)
  respKey=coldict['key_resp.keys']
  for ans in respKey:
    d[ans]+=1	
  print 'number times answered BA: ' + str(d['1'])
  print 'number times answered WA: ' + str(d['2'])
  print 'number times answered Noise: ' + str(d['3'])
  
  stims=['ba_n75db.wav','bam_n75db.wav','baf_n75db.wav',
  		'wa_n75db.wav','wam_n75db.wav','waf_n75db.wav',
  		'bawa_n75db.wav','bawam_n75db.wav','baf_n75db.wav']
  
  #calculate frequency of stim files
  f=defaultdict(int)
  fileName=coldict['stim']
  for name in fileName:
  	f[name]+=1.0
  freqBa=f[stims[0]]+f[stims[1]]+f[stims[2]]
  freqWa=f[stims[3]]+f[stims[4]]+f[stims[5]]
  freqBawa=f[stims[6]]+f[stims[7]]+f[stims[8]]
  freqSynth=f[stims[0]]+f[stims[3]]+f[stims[6]]
  freqF=f[stims[2]]+f[stims[5]]+f[stims[8]]
  freqM=f[stims[1]]+f[stims[4]]+f[stims[7]]
	  
  
  #calculations
  a=defaultdict(int)
  for name, ans in zip(fileName,numcorr):
  	ans=int(ans)
  	a[name]+=ans
  numSynthCorr=a[stims[0]]+a[stims[3]]+a[stims[6]]
  numMaleCorr=a[stims[1]]+a[stims[4]]+a[stims[7]]
  numFemCorr=a[stims[2]]+a[stims[5]]+a[stims[8]]
  numBaCorr=a[stims[0]]+a[stims[1]]+a[stims[2]]
  numWaCorr=a[stims[3]]+a[stims[4]]+a[stims[5]]
  numBawaCorr=a[stims[6]]+a[stims[7]]+a[stims[8]]
  print 'Raw Ba correct: ' +str(numBaCorr)
  print 'percentage Ba correct: ' +str(numBaCorr/freqBa*100) + '%'
  print 'Raw Wa correct: ' +str(numWaCorr)
  print 'pecentage Wa correct: ' +str(numWaCorr/freqWa*100) +'%'
  print 'Raw BaWa correct: ' +str(numBawaCorr)
  print 'percentage BawWa correct: ' +str(numBawaCorr/freqBawa*100) + '%'
  print 'Raw synthetic correct: ' +str(numSynthCorr)
  print 'percentage synthetic correct: ' +str(numSynthCorr/freqSynth*100) +'%'
  print 'Raw Male correct: ' +str(numMaleCorr)
  print 'percentage Male correct: ' +str(numMaleCorr/freqM*100) +'%'
  print 'Raw Female correct: ' +str(numFemCorr)
  print 'percentage Female correct: ' +str(numFemCorr/freqF*100) +'%'
  print 'Raw Human correct: ' +str(numFemCorr+numMaleCorr)
  print 'percentage Human correct: ' +str((numFemCorr+numMaleCorr)/(freqM+freqF)*100) + '%'
  
  counterW=0
  counterB=0
  for name, resp in zip(fileName,respKey):	
  	if   (name==stims[0] or name==stims[1] or name==stims[2]) and resp=='2':
  		 counterW +=1
  	elif (name==stims[0] or name==stims[1] or name==stims[2]) and resp=='1':
  		 counterB +=1 
  print 'Raw Bawa-b: ' +str(counterB)
  print 'Percentage Bawa-b: ' +str(counterB/15.0*100) + '%'
  print 'Raw Bawa-w: ' +str(counterW)
  print 'Percentage Bawa-w: ' + str(counterW/15.0*100) + '%'
  

if __name__ == '__main__':
  main()

