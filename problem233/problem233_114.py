n=int(input())
p=list(map(int,input().split()))

check=200001
cnt=0
for i in p:
	if check > i:
		check = i
		cnt+=1
print(cnt)