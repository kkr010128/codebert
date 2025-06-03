n, x, y = map(int, input().split())
x -= 1
y -= 1


def shortest_path(i, j):
    res = min(abs(i-x)+abs(j-y)+1, j-i)
    return res


ans = [0]*(n-1)
for i in range(n-1):
    for j in range(i+1, n):
        d = shortest_path(i, j)
        ans[d-1] += 1

print(*ans, sep='\n')
