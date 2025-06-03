import sys
input = sys.stdin.readline

# D - Triangles
def binary_search(i, j):
	global N

	left = j
	right = N
	
	while right - left > 1:
		mid = (left + right) // 2
		
		if is_match(mid, i, j):
			left = mid
		else:
			right = mid
	
	return left
		

def is_match(mid, i, j):
	global L
	
	a = L[i]
	b = L[j]
	c = L[mid]
	
	if b < c + a and c < a + b:
		return True
	else:
		return False


N = int(input())
L = list(map(int, input().split()))
L.sort()

ans = 0

for i in range(N - 2):
	for j in range(i + 1, N - 1):
		k = binary_search(i, j)
		
		if k > j and k < N:
			ans += k - j
			
print(ans)