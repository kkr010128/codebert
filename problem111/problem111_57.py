N=int(input())
A=list(map(int,input().split()))
A.sort(reverse=True)
cnt=2
ans=A[0]
i=1
while cnt<N:
	ans+=A[i]
	if (cnt+1)%2==0:
		i+=1
	cnt+=1
print(ans)