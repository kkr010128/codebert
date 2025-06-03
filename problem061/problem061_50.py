old_char = raw_input()
new_char = ""
for i in old_char:
	if i.islower():
		new_char += i.upper()
	elif i.isupper():
		new_char += i.lower()
	else:
		new_char += i
print new_char