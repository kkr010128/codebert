# Belongs to : midandfeed aka asilentvoice
s = str(input())
ans = ""
for i in range(len(s)):
	if s[i] == s[i].lower():
		ans += s[i].upper()
	else:
		ans += s[i].lower()
		
print(ans)