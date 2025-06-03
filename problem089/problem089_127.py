#!/usr/bin/python3
# -*- coding:utf-8 -*-

import numpy
from collections import defaultdict

def main():
  h, w, m = map(int, input().strip().split())
  fieldh = numpy.zeros(h, dtype=numpy.int)
  fieldw = numpy.zeros(w, dtype=numpy.int)
  field = defaultdict(int)
  for _ in range(m):
    ih, iw = map(int, input().strip().split())
    fieldh[ih-1] += 1
    fieldw[iw-1] += 1
    field[ih-1, iw-1] = 1
    
  max_h = numpy.max(fieldh)
  max_w = numpy.max(fieldw)
  argsort_h = [ ih for ih in range(h) if fieldh[ih] == max_h ]
  argsort_w = [ iw for iw in range(w) if fieldw[iw] == max_w ]
  
  max_cnt = 0
  for ih in argsort_h:
    for iw in argsort_w:
      if field[ih, iw] == 0:
        max_cnt = max(max_cnt, fieldh[ih]+fieldw[iw])
        print(max_cnt)
        return 
      else:
        max_cnt = max(max_cnt, fieldh[ih]+fieldw[iw]-1)
  print(max_cnt)

if __name__=='__main__':
  main()

