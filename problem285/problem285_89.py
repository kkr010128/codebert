s = input()
A = [0] * (len(s) + 1)
for i, c in enumerate(s):
	if c == '<':
		A[i+1] = A[i] + 1
for i, c in enumerate(s[::-1]):
	if c == '>':
		x = len(s) - i
		A[x-1] = max(A[x-1], A[x] + 1)
print(sum(A))