import sys; input = sys.stdin.readline
# n, m , k = map(int, input().split())
# matrix = [list(input().strip()) for _ in range(n)]

n = int(input())
lis = sorted(map(int, input().split()), reverse=True)
ans = lis[0]
i = 1
c = 1
while c<n-1:
	if c < n-1: ans += lis[i]; c+=1
	if c < n-1: ans += lis[i]; c+=1
	i+=1
print(ans)

