N = int(input())
L = list(map(int, input().split()))

ans = 0
for i1 in range(N):
    for i2 in range(i1, N):
        for i3 in range(i2, N):
            l1 = L[i1]
            l2 = L[i2]
            l3 = L[i3]
            if l1 != l2 and l2 != l3 and l3 != l1:
                if l1 < l2 + l3 and l2 < l3 + l1 and l3 < l1 + l2:
                    ans += 1

print(ans)
