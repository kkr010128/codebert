# B - Iron Bar Cutting
N = int(input())
A = list(map(int, input().split()))

left = 0
right = sum(A)
ans = right

for a in A:
	left += a
	right -= a
	
	diff = abs(right - left)
	ans = min(ans, diff)
	
	if left > right:
		break

print(ans)
