import sys
n=int(input())
a=[]
b=[]
for i in range(n):
  s=input()
  overall=0
  minimum=0
  current=0
  for j in range(len(s)):
    if s[j]=='(':
      current+=1
    else:
      current-=1
    minimum=min(current,minimum)
  overall=current
  if overall>=0:
    a.append([overall,minimum])
  else:
    b.append([overall,minimum])
finalsum=0
a=sorted(a, key=lambda t:t[1])
a.reverse()
b=sorted(b, key=lambda t:t[0]-t[1])
b.reverse()
for i in a:
  if finalsum+i[1]<0:
    print('No')
    sys.exit()
  finalsum+=i[0]
for i in b:
  if finalsum+i[1]<0:
    print('No')
    sys.exit()
  finalsum+=i[0]
if finalsum==0:
  print('Yes')
else:
  print('No')