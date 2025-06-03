s = input()
st1=[]
st2=[]
st3=[]
total=0
for i in range(len(s)):
	c=s[i]
	if c=='\\':
		st1.append(i)
	elif c=='/':
		if len(st1) > 0:
			j = st1.pop()
			a = i - j
			total+=a
			tmp=0
			while len(st2)>0 and st2[-1]>j:
				st2.pop()
				tmp+=st3.pop()
			st3.append(a+tmp)
			st2.append(j)
			
print(total)
n = len(st3)
print(n,end='')
for i in range(n):
	print(' '+str(st3[i]),end='')
print()

