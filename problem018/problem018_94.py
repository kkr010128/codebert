n=input().split()
c=0
while len(n)!=1:
	if n[c]=='+':
		n[c-2]=int(n[c-2])+int(n[c-1])
		del n[c-1]
		del n[c-1]
		c=0
	elif n[c]=='-':
		n[c-2]=int(n[c-2])-int(n[c-1])
		del n[c-1]
		del n[c-1]
		c=0
	elif n[c]=='*':
		n[c-2]=int(n[c-2])*int(n[c-1])
		del n[c-1]
		del n[c-1]
		c=0
	elif n[c]=='/':
		n[c-2]=int(n[c-2])/int(n[c-1])
		del n[c-1]
		del n[c-1]
		c=0
	c+=1
a=int(n[0])
print(a)
