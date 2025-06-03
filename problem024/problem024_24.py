n, k = map(int, input().split())
wlist = []
for i in range(n):
    wlist.append(int(input()))

ma = sum(wlist) + 1
mi = max(wlist) - 1
while (ma - mi > 1):
    mid = (ma + mi)//2
    truck = [0for i in range(k)] ## k개
    i = 0
    gobigger = 0
    for w in wlist:
        if(truck[i] + w <= mid):
            truck[i] = truck[i] + w
        else:
            i = i+1
            if (i == k):
                gobigger = 1
                break
            truck[i] = truck[i] + w
    if (gobigger == 1):
        mi = mid
    else:
        ma = mid
    
print(ma)
        
