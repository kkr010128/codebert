n=int(input())
a=list(map(int,input().split()))
ans=10**20
p=sum(a)
q=0
for i in range(n-1):
	q+=a[i]
	ans=min(ans,abs(p-q-q))
print(ans)
