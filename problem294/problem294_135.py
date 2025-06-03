def biserch(n,List):
    left = 0
    right = len(List)
    while left < right:
        mid = (left+right)//2
        if n <= List[mid]:
            right = mid
        else:
            left = mid + 1
    
    return left
    
N = int(input())
L = list(map(int,input().split()))
L.sort()

ans = 0
for i in range(N):
    for j in range(i+1,N):
        key = L[i] + L[j]
        anchor = biserch(key,L)
        
        ans += max(anchor - (j+1),0)

print(ans)