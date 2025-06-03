x = int(input())
p = list(map(int, input().split()))

if len(set(p)) == len(p):
	print("YES")
else:
	print("NO")