N=int(input())
P=[int(x) for x in input().split()]

minP=P[0]
cnt=0
for p in P:
  if p<=minP:
    cnt+=1
  minP=min(minP, p)

print(cnt)