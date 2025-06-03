N = int(input())
*A, = map(int, input().split())
ans = 0
for i, a in enumerate(A):
    if (i + 1) & 1 and a & 1:
        ans += 1
print(ans)
