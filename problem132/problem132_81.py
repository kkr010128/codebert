n,k,*l=map(int,open(0).read().split())
for _ in range(min(k,41)):
  s=[0]*-~n
  for i in range(n):
    s[max(i-l[i],0)]+=1
    s[min(i+l[i]+1,n)]-=1
  for i in range(n): s[i+1]+=s[i]
  l=s
print(*l[:n])