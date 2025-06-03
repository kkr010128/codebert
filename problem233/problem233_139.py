n=int(input())
listn=list(map(int,input().split()))
count=0
min1=listn[0]
for i in range(0,n):
	if(listn[i]>min1):
		pass
	else:
		min1=listn[i]
		count+=1
print(count)
