str = input()
new = ''
for i in str:
	if i.islower():
		new +=  i.upper()
	else:
		new += i.lower()
print(new)