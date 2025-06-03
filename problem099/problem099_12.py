# 2butan renshuu 0812

def f(m):
  cut=0
  for aa in a:
    cut+=(aa-1)//m
    if cut > k:
      return False
  return True

n,k=map(int,input().split())
a=list(map(int,input().split()))

l=0
r=10**9+1
while r-l>1:
  m=(l+r)//2
  # right move
  if f(m):
    r=m
  else:
    l=m

print(r)
