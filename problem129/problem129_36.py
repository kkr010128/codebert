n = int(input())

a = [int(x) for x in input().split()]

baisuu=[0]*(10**6+1)

for i in a:
	if baisuu[i]>=1:
		baisuu[i]=2
		continue

	for j in range(i,10**6+1,i):
		baisuu[j]+=1

ans=0

for i in a:
	if baisuu[i]==1:
		ans+=1

print(ans)