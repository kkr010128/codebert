S = input()
q = int(input())

for i in range(q):
	L = input().split()
	a = int(L[1])
	b = int(L[2])
	slice1 = S[:a]
	slice2 = S[a:b+1]
	slice3 = S[b+1:]
	if L[0] == 'print':
		print(slice2)
	elif L[0] == 'reverse':
		S = slice1 + slice2[::-1] + slice3
	elif L[0] == 'replace':
		S = slice1 + L[3] + slice3