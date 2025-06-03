import heapq
n,k = map(int,input().split())
a = [int(i) for i in input().split()]

low = 0
high = 10**9

if k == 0:
    print(max(a))
    exit()

    
while low+1 < high:
    tmp = 0
    mid = (low + high) //2
    
    for i in range(n):
        tmp += ((a[i]+mid-1) // mid)-1
        
    if tmp <= k:
        high = mid
    else:
        low = mid
        
print(high)
