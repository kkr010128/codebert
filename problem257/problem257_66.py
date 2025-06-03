N=int(input())
A=[int(x) for x in input().split()]
start=0
for i in A:
  if (start+1)==i:
    start+=1
if start!=0:
  print(len(A)-start)
else:
  print(-1)