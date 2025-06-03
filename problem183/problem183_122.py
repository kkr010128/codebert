n=int(input())
p=n
yakusu=[]
for i in range(1,int(n**0.5)+1):
	if n%i==0:
		yakusu.append(i)
		if i!=n//i:
			yakusu.append(n//i)
p-=1
yakusu_1=[]
for i in range(1,int(p**0.5)+1):
	if p%i==0:
		yakusu_1.append(i)
		if i!=p//i:
			yakusu_1.append(p//i)
ans=len(yakusu_1)-1
for x in yakusu:
	r=n
	if x!=1:
		while r%x==0:
			r//=x
		if (r-1)%x==0:
			ans+=1
print(ans)