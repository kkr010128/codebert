import sys
n=int(input())
s=[list(input()) for i in range(n)]
L1=[]
L2=[]
for i in range(n):
  ct3=0
  l=[0]
  for j in s[i]:
    if j=='(':
      ct3+=1
      l.append(ct3)
    else:
      ct3-=1
      l.append(ct3)
  if l[-1]>=0:
    L1.append((min(l),l[-1]))
  else:
    L2.append((min(l)-l[-1],-l[-1]))

L1.sort()
L1.reverse()
ct4=0
for i in L1:
  if ct4+i[0]<0:
    print('No')
    sys.exit()
  ct4+=i[1]

L2.sort()
L2.reverse()
ct5=0
for i in L2:
  if ct5+i[0]<0:
    print('No')
    sys.exit()
  ct5+=i[1]

if ct4!=ct5:
  print('No')
  sys.exit()

print('Yes')