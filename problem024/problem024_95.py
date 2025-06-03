n, k = map(int, input().split())
wList = []
for i in range(n):
    w = int(input())
    wList.append(w)
minP = max(wList)-1
maxP = sum(wList)
def countD(mid, wList):
    curr = 0
    count = 0
    for w in wList:
        if curr+w > mid:
            count+=1
            curr = w
        else:
            curr+=w
    if curr > 0:
        count+=1
    return count
while maxP - minP > 1:
    mid = (minP + maxP)//2
    days = countD(mid, wList)
    if days <= k:
        maxP = mid
    else:
        minP = mid
print(maxP)
