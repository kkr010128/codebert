# -*- coding: utf-8 -*-
N = int(input())
S = list()
words = {}
for i in range(N):
  s = input()
  S.append(s)
  if s in words:
    words[s] += 1
  else:
    words[s] = 1

max_value = max(words.values())
max_list = list()
for k,v in words.items():
  if v == max_value:
    max_list.append(k)
ans_list = sorted(max_list)
for ans in ans_list:
  print(ans)