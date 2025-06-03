n=int(input())
p=list(map(int,input().split()))

check=200001
cnt=0
for i in range(n):
	if check > p[i]:
		check = p[i]
		cnt+=1
print(cnt)