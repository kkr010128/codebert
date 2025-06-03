n,k=map(int,input().split())
a=list(map(int,input().split()))

cnt=0

for i in range(n-k):
	if a[cnt]<a[cnt+k]:
		print("Yes")
        
	else:
		print("No")

	cnt+=1
    