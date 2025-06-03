n=input()
a=map(int,raw_input().split())

INF=10**18

pr=[0]*(n+2)

pr[0]=1

for i in xrange(n+1):
	pr[i+1]=min(INF,(pr[i]-a[i])*2)

if pr[n+1]<0:
	print "-1"
	exit(0)

s=0
ans=0

for i in xrange(n,-1,-1):
	s=min(s+a[i],pr[i])
	ans+=s

print ans