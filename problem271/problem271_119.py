
n = int(input())
a = input()
ans = ""
for i in a:
	ans += chr(65 + (ord(i) - 65 + n )%26)
print(ans)