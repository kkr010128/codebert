n=int(input())
dic={}
a=[]
b=[]
for i in range(n):
	tmp1,tmp2=input().split()
	a.append(tmp1)
	b.append(tmp2)

for i in range(n):
	if a[i]=='insert':
		dic[b[i]]=1
	else:
		if b[i] in dic:
			print("yes")
		else:
			print("no")
