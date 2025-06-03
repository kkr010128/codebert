x1, v1 = map(int, input().split(' '))
x2, v2 = map(int, input().split(' '))
t = int(input())

p = abs(x2 - x1)
q = (v1 - v2) * t
if p <= q:
	print("YES")
else:
	print("NO")