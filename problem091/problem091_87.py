n=int(input())
r=list(map(int,input().split()))
t=0
for i in range(n):
	for j in range(i+1,n):
		for k in range(j+1,n):
			if r[i]==r[j] or r[j]==r[k] or r[i]==r[k]:continue
			s=[r[i],r[j],r[k]]
			s.sort()
			if s[0]+s[1]>s[2]:
				t+=1
print(t)