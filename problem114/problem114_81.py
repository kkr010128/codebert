D = int(input())
c = [int(x) for x in input().split()]
s = []
for i in range(D):
    s.append([int(x) for x in input().split()])
ans = 0
nissuu = [0] * 26
for i in range(D):
    t = int(input())
    for j in range(26):
        if j == t-1:
            nissuu[j] = 0
        else:
            nissuu[j] += 1
        ans -= c[j]*nissuu[j]
    ans += s[i][t-1]
    print(ans)