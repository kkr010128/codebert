s=input()
res=""
for t in s:
	if t.islower()==True:
		res+=t.upper()
	else:
		res+=t.lower()


print(res)
