N = int(input())
L = list(map(int, input().split()))

L.sort()
ans = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i < j < k and L[i] < L[j] < L[k] and L[i] + L[j] > L[k]:
                ans += 1

print(ans)
