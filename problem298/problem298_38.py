n,k=map(int,input().split())
hlist=list(map(int,input().split()))

counter=0
for h in hlist:
	if h >= k:
		counter += 1
print(counter)