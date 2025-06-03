import string
alphabet = list(string.ascii_lowercase)
n = int(input())
ans = []
while n > 0:
	o = (n-1) % 26
	n = (n-1) // 26
	ans.append(alphabet[o])
ans.reverse()
print("".join(ans))