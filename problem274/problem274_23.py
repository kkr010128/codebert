n,k=map(int,input().split())
h=input()

cnt=0
for i in range(n):
	if h[i]=="1":
		cnt+=1
	else:
		cnt=0
	if cnt>=k:
		print(-1)
		exit()

h=h[::-1]
h+="0"
idx=0
ans=[]
while 1:
	if idx+k>=n:
		ans.append(n-idx)
		break
	for i in range(k,0,-1):
		if h[idx+i]=="0":
			ans.append(i)
			idx+=i
			break
ans=reversed(ans)
print(" ".join([str(x) for x in ans]))
