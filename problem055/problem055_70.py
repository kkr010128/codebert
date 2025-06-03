A = []
for _ in range(12):
	A.append([0]*10)

n = int(input())
for _ in range(n):
	b, f, r, v = map(int, input().split())
	A[3*b-(3-f)-1][r-1] += v

for i in range(12):        
	print(' ', end='')
	print(' '.join(map(str, A[i])))
	if i in [2, 5, 8]:
		print('#'*20)
