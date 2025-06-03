from math import ceil
n = int(input())
ans = 0
for i in range(1, n):
    for j in range(1, n // i + 1):
        if i * j != n:
            #print(i, j, n - i * j)
            ans += 1
print(ans)