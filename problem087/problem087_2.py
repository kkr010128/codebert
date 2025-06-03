total = 0
for ch in input().strip():
	total = (total + int(ch)) % 9
print('No' if total else 'Yes') 