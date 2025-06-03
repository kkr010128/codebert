import sys

n=int(input())
d=[]
cnt=0

for i in range(n):
  D=[int(x) for x in input().split()]
  d.append(D)

for d1,d2 in d:
  if d1==d2:
    cnt+=1
  else:
    cnt=0
  if 3<=cnt:
    print("Yes")
    sys.exit()

print("No")