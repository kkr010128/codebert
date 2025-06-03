A, B, M = map(int, input().split())
an = list(map(int, input().split()))
bn = list(map(int, input().split()))
ans = min(an)+min(bn)
for i in range(M):
    x, y, c = map(int, input().split())
    ans = min(ans, an[x-1] + bn[y-1] - c)
print(ans)
