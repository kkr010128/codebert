def ev(n):
    return (n+1) / 2


N, K = map(int, input().split())
p = list(map(int, input().split()))
prev = ev(p[0])
ans = sum([ev(i) for i in p[:K]])
total = ans

for i in range(1, N-K+1):
    total -= prev
    total += ev(p[i+K-1])
    prev = ev(p[i])
    ans = max(ans, total)

print(ans)
