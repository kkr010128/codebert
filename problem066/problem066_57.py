ss = str(input())
while (ss != '-'):
    slist = []
    for s in ss:
        slist.append(s)
    m = int(input())
    for i in range(m):
        n = int(input())
        for k in range(n):
            slist.append(slist[k])
        for k in range(n):
            del slist[0]
    for i in range(len(slist)):
        print(slist[i], end = '')
    print()
    ss = str(input())
        
