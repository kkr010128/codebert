n,m=map(int,input().split())
su=input()
rev=su[::-1]
if "1"*m in su:
	print(-1)
	exit()
dist_f_n=[float('inf')]*(n+1)
dist_f_n[0]=0
for i in range(1,m+1):
	if rev[i]=="0":
		dist_f_n[i]=1
		last=i
		if i==n:
			break
while last<n:
	for i in range(last+1,last+m+1):
		if rev[i]=="0":
			dist_f_n[i]=dist_f_n[last]+1
			_last=i
			if i==n:
				break
	last=_last
cur=dist_f_n[-1]
_i=0
ans=[]
for i,x in enumerate(dist_f_n[::-1]):
	if x==cur-1:
		ans.append(i-_i)
		cur-=1
		_i=i
print(" ".join(map(str,ans)))
