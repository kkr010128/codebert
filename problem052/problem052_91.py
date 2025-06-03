n=input()
n=int(n)
s=""
for i in range(1,n+1):
	if i%3==0:
		s+=" "+str(i)
	elif "3" in list(str(i)):
		s+=" "+str(i)
print(s)