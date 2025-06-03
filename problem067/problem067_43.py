
s=[0,0]
for i in range(int(input())):
	r=input().split()
	if r[0]<r[1]:
		s[1]+=3
	elif r[1]<r[0]:
		s[0]+=3
	else:
		s[0]+=1
		s[1]+=1
print(str(s[0])+' '+str(s[1]))
