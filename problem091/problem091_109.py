n = int(input())
L = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if L[i] == L[j] or L[j] == L[k] or L[k] == L[i]:
                pass
            elif L[i] + L[j] > L[k] and L[j] + L[k] > L[i] and L[k] + L[i] > L[j]:
                ans += 1
print(ans)