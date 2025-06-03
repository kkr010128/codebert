N = int(input())
S = list(map(int,input().split()))

if N < 3:
  print(0)
  exit(0)

import itertools as it
per = it.combinations(S,r=3)

cnt = 0
for r in per:
  a,b,c = r
  if a ==  b or b == c or a == c:
    continue
    
  if a+b > c and b+c > a and a+c > b:
    #print(a,b,c)
    cnt += 1
    
print(cnt)
