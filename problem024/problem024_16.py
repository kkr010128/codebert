#coding: utf-8
n, k = map(int, input().split())
pkt = list()
for i in range(n):
    pkt.append(int(input()))
lenpkt = len(pkt)

def maxPkt(payload):
    maxPnum = 0
    for i in range(k):
        tempPL = 0
        while tempPL + pkt[maxPnum] <= payload:
            tempPL += pkt[maxPnum]
            maxPnum += 1
            if maxPnum == lenpkt:
                return True
    return False

lft = 0
mid = 0
rgt = 100000 * 10000

while lft < rgt:
    mid = (lft + rgt) // 2
    if maxPkt(mid):
        rgt = mid
    else:
        lft = mid + 1

print(rgt)
