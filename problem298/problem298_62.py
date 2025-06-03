n,k=[int(s) for s in input().split()]
h=[int(j) for j in input().split()]
r=0

for i in range(n):
  if k<=h[i]:
    r=r+1
  

print(r)