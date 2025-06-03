n,k=map(int,input().split())
a=list(map(int,input().split()))

def imos(a):
  imos_l=[0 for i in range(n)]

  for i in range(n):
    left=max(i-a[i],0)
    right=min(i+a[i],n-1)

    imos_l[left]+=1
    if right+1!=n:
      imos_l[right+1]-=1

  b=[0]
  for i in range(1,n+1):
    b.append(b[i-1]+imos_l[i-1])

  return b[1:]

for i in range(k):
  a=imos(a)
  if a.count(n)==n:
    break

print(*a)