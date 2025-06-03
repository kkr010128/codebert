N,M=map(int,input().split())
H=list(map(int,input().split()))
H.insert(0,0)
s=set()
for i in range(M):
  a,b=map(int,input().split())
  if H[a]<=H[b]:s.add(a)
  if H[a]>=H[b]:s.add(b)
print(N-len(s))