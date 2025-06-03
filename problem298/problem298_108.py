N,K = [int(i) for i in input().split()]
H = [int(i) for i in input().split()]

ans = 0
for i in range(N):
    if K <= H[i]:
        ans += 1

print(ans)
