H,W,K=map(int,input().split())
c_map=[]
for _ in range(H):
	c=input()
	c_map.append(c)

ans=0

for i in range(2**H):
	for j in range(2**W):
		cnt=0
		for k in range(H):
			for l in range(W):
				if c_map[k][l]=='#' and (i>>k)&1==0 and (j>>l)&1==0:
					cnt+=1
		if cnt==K:
			ans+=1

print(ans)