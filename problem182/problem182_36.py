n,k,c=map(int,input().split())
s=list(input())
for i in range(len(s)):
	if s[i]=="o":
		s[i]=True
	else:
		s[i]=False
i=0
work1=[]
while len(work1)<k:
	if s[i]:
		work1.append(i)
		i+=c+1
	else:
		i+=1
i=n-1
work2=[]
while len(work2)<k:
	if s[i]:
		work2.append(i)
		i-=c+1
	else:
		i-=1
work2.sort()
for i in range(k):
	if work1[i]==work2[i]:
		print(work1[i]+1)