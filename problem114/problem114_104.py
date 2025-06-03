D = int(input())
c = [int(i) for i in input().split()]
s = [[int(i) for i in input().split()] for _ in range(D)]
t = [int(input())-1 for _ in range(D)]
ans = 0
llst = [0]*26

for day,i in enumerate(range(D),1):
    llst[t[i]] = day
    ans += s[i][t[i]]
    for j in range(26): ans -= c[j]*(day-llst[j])
    print(ans)