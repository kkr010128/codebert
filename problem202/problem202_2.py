N, A, B = map(int, input().split())
ans = 0
roop = int(N / (A + B))
# print(roop)
padding = N % (A + B)
if padding >= A:
    ans += roop * A + A
else:
    ans += roop * A + padding

print(ans)