n, k = map(int, input().split())

def cul(x):
    ans = (1 + x)*x/(2*x)
    return ans

p = list(map(cul, list(map(int, input().split()))))
cnt = sum(p[0:k])
ans = cnt
for i in range(k, n):
    cnt += p[i] - p[i - k]
    ans = max(ans, cnt)
print(ans)