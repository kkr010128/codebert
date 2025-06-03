n = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if len(list(set([L[i], L[j], L[k]]))) < 3:
                continue
            if L[i] + L[j] <= L[k]:
                continue
            ans += 1
print(ans)
