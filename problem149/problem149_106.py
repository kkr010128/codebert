n, m, x = map(int, input().split())
ca = [(list(map(int, input().split()))) for _ in range(n)]
caca = [0]*(m+1)
ans = 12 * 10**5 +1
chk = 0
for nn in range(2**n):
    for j in range(m+1):
        caca[j] = 0
    cnt = 0
    for i in range(n):
        if (nn>>i) & 1:
            for j in range(m+1):
                caca[j] += ca[i][j]
    for j in range(1, m+1):
        if caca[j] >= x:
            cnt += 1
        else:
            break
    if cnt == m:
        ans = min(ans, caca[0])
        chk = 1
print(ans if chk == 1 else -1)