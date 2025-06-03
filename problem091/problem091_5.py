n = int(input())
L = [int(x) for x in input().split()]
L.sort()
ans = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if L[i] != L[j] != L[k]:
                if L[i] + L[j] > L[k]:
                    ans += 1

print(ans)
