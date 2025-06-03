n ,q = map(int, input().split())
ntlist = []
for i in range(n):
    nt = list(map(str, input().split()))
    ntlist.append(nt)
tp = 0
while (len(ntlist)):
    nt = ntlist.pop(0)
    if (int(nt[1])> q):
        nt[1] = int(nt[1]) - q
        tp += q
        ntlist.append(nt)
    else:
        tp += int(nt[1])
        nt[1] = 0
        print(nt[0], tp)

