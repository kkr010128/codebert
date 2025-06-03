k = int(input())
S = input()

if k >= len(S):
	print(S)
else:
	ans = S[0:k]
	dots = '...'
	print(ans + dots)