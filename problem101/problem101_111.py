A, B, C = map(int, input().split())
K = int(input())

while B <= A and K:
	B *= 2
	K -= 1

while C <= B and K:
	C *= 2
	K -= 1

print('Yes' if A < B < C else 'No')
