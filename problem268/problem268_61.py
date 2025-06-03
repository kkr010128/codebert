M = 1000000007
N = int(input())
A = list(map(int, input().split()))

ans = 1
rgb = [0, 0, 0]
for i in range(N):
    c = rgb.count(A[i])
    if c == 0:
        ans = 0
        break
    p = rgb.index(A[i])
    ans *= c
    rgb[p] += 1

print(ans % M)