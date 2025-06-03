import bisect
n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
r=a[n-1]*2+1
l=0
while r-l>=2:
	mid=(l+r)//2
	#mid以上はいくつあるか
	#答えはl以上r未満
	cnt=0
	for i in range(n):
		cnt+=n-bisect.bisect_left(a,mid-a[i])
	if cnt>=k:
		l=mid
	else:
		r=mid
#lだとk個以上　rだとk個未満
ans,p,=0,0
b=[0]
for i in range(n):
	p+=a[i]
	b.append(p)
for i in range(n):
	q=bisect.bisect_left(a,r-a[i])
	ans+=b[n]-b[q]
	ans+=a[i]*(n-q)
	k-=n-q
ans+=l*k
print(ans)
