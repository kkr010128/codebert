N, L = int(input()), [int(v) for v in input().split()]
L.sort()
ans = 0
for i in range(N):
    for j in range(i):
        for k in range(j):
            if L[k] != L[j] and L[j] != L[i] and L[k] + L[j] > L[i]:
                    ans += 1

print(ans)