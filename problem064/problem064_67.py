s=raw_input()
target=raw_input()
ring=s*2

ans="No"
for i in range(len(s)):
	if ring[i:i+len(target)]==target:
		ans="Yes"
		break
print ans