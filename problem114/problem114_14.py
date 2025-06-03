d = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for i in range(d)]
t = [int(input()) for i in range(d)]
ans = 0
l = [0 for i in range(26)]
for i in range(d):
    ans += s[i][t[i] - 1]
    l = list(map(lambda x:x+1, l))
    l[t[i] - 1] = 0
    for j in range(26):
        ans -= c[j] * l[j]
    print(ans)