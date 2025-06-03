n,m = map(int,input().split())
sub = []
for i in range(m):
    tmp= [x for x in input().split()]
    sub.append(tmp)
ac = [0]*n
wa = [0]*n
for i in range(m):
    res = sub[i][1]
    que = int(sub[i][0]) - 1
    if res == "AC" and ac[que] == 0:
        ac[que] += 1
    elif res == "WA" and ac[que] == 0:
        wa[que] += 1
for i in range(n):
    if ac[i] != 1:
        wa[i] = 0
print(sum(ac),sum(wa))



    
