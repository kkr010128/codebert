# -*= coding: utf-8 -*-
from collections import deque

S = input()
Q = int(input())
query = list()
for i in range(Q):
  query.append(list(map(str, input().split())))


d = deque()
for s in S:
  d.append(s) # 右からsを追加
is_reverse = False

for q in query:
  if len(q) == 1:
    # Tiが1の場合
    
    is_reverse = not is_reverse
    
  else:
    # Tiが2の場合
    
    if q[1] == '1':
      # Fiが1の場合
      
      if is_reverse == False:
        d.appendleft(q[2])
      else:
        d.append(q[2])
      
    else:
      # Fiが2の場合
      
      if is_reverse == False:
        d.append(q[2])
      else:
        d.appendleft(q[2])

ans = ''
if is_reverse == True:
  d.reverse()
ans = ''.join(d)
print(ans)