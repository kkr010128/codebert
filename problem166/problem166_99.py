s=list(map(int,input()))
c=0
cnt=[0]*2019
cnt[0]+=1
for k in range(len(s)-1,-1,-1):
	c=(c+s[k]*pow(10,len(s)-1-k,2019))%2019
	cnt[c]+=1
print(sum(x*(x-1)//2 for x in cnt))