# -*- coding: utf-8 -*-
from sys import stdin

Dic = {}
n = int(stdin.readline().rstrip())
for i in range(n):
  line = stdin.readline().rstrip()
  if line[0] == 'i':
    Dic[line[7:]] = 0
  else:
    print('yes' if line[5:] in Dic else 'no')
