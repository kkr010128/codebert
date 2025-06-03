N = int(input())
A = list(map(int, input().split()))
mod = 10**9+7

RGB = [0, 0, 0]

ans = 1
for i in range(N):
    cnt = RGB.count(A[i])
    ans = (ans * cnt) % mod
    for j in range(3):
        if A[i] == RGB[j]:
            RGB[j] += 1
            break

print(ans)
