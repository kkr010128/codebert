n = int(input())
tscore = 0
hscore = 0
for i in range(n):
    wlist = []
    t,h = map(str, input().split())
    wlist.append(t)
    wlist.append(h)
    order = sorted(wlist, key = str.lower)
    if (t.lower() == h.lower()):
        tscore += 1
        hscore += 1
    elif (order[1] == t):
        tscore += 3
    elif (order[1] ==h ):
        hscore += 3
print(tscore, hscore)
        
