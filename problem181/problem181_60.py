# -*- coding: utf-8 -*-
import queue
K = int(input())
q = queue.Queue()

count = 0
for i in range(1, 10):
  q.put(i)

a = 0
while count < K:
  
  a = q.get()
  fp = int(str(a)[-1])
  if fp == 0:
    q.put(a*10)
    q.put(a*10 + 1)
  elif fp == 9:
    q.put(a*10 + 8)
    q.put(a*10 + 9)
  else:
    q.put(a*10 + fp - 1)
    q.put(a*10 + fp)
    q.put(a*10 + fp + 1)
  count += 1

print(a)