N = int(input())
a = list(map(int, input().split()))
x = 0

for r in a:
	x ^= r
a = [str(x^r) for r in a]
a = ' '.join(a)
print(a)