d = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for i in range(d)]
lastd = [0] * 26

for i in range(1, d + 1):
    ans = 0
    tmp = 0
    for j in range(26):
        if tmp < s[i - 1][j] + (i - lastd[j]) * c[j]:
            tmp = s[i - 1][j] + (i - lastd[j]) * c[j]
            ans = j + 1
    lastd[ans - 1] = i
    print(ans)