d=int(input())
c=list(map(int,input().split()))
s=[list(map(int,input().split())) for _ in range(d)]
C=sum(c)
tot=0
mem=[0]*26
for i in range(d):
	t=int(input())
	mem[t-1]=i+1
	tot+=s[i][t-1]
	for j in range(26):
		tot-=c[j]*((i+1)-mem[j])
	print(tot)