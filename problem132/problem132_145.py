n, K = map(int, input().split())
a = list(map(int, input().split()))
s = [[0]*n for _ in range(100)]
s[0] = a

tmp = [0] * (n+1)
for i in range(K):
    if sum(s[i]) == n**2:
        print(*([n] * n))
        break
    for j in range(n):
        x = s[i][j]
        l, r = max(0, j-x), min(n, j+x+1)
        tmp[l] += 1
        tmp[r] -= 1
    
    for j in range(n):
        tmp[j+1] = tmp[j] + tmp[j+1]
        s[i+1][j] += tmp[j]
    tmp = [0] * (n+1)
else: print(*s[K])
