s=input()
tex=[]
while 1:
	a=input()
	if a=="END_OF_TEXT":
		break
	else:
		tex.extend([x.lower() for x in a.split()])

c=0
tex

for i in tex:
	if i==s:
		c+=1

print(c)