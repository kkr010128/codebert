n = int(input())
f = 0
L = []
for i in range(n):
	a,b = map(int, input().split())
	L.append([a,b])
for i in range(2,n):
	if(L[i-2][0] == L[i-2][1] and L[i-1][0] == L[i-1][1] and L[i][0] == L[i][1]):
		f = 1
		break
if(f):
	print('Yes')
else:
	print('No')