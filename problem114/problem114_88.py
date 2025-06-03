d = int(input())
c = list(map(int,input().split()))
s = []
day = [0 for i in range(26)]
for i in range(d):
    s.append(list(map(int,input().split())))
ans = 0
num = 1
for i in range(d):
    t = int(input())-1
    day[t] = num
    for j in range(26):
        if j == t:
            ans += s[i][j]
        else:
            ans -= c[j]*(num-day[j])
    print(ans)
    num += 1