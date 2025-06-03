N, K = map(int, input().split())

p = input().split()
p = [int(s) for s in p]
p.sort()

ans = 0
for i in range(K):
    ans += p[i]
print(ans)