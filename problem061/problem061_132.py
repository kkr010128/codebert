str = input()

for char in str:
	if char.islower():
		print(char.upper(), end='')
	else:
		print(char.lower(), end='')
print("");