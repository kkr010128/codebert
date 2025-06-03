#E
N,K = map(int,input().split())
A = list(map(int,input().split()))
F = list(map(int,input().split()))

A.sort(reverse=True)
F.sort()

left = 0
right = 10**12
while True:
    mid = (left+right)//2
    if right - left <= 1:
        count = 0
        for i in range(N):
            a = left//F[i]
            count+=max(0,A[i]-a)
        if count <= K:
            ans = left
        else:
            ans = right
        break
    
    
    count = 0
    for i in range(N):
        a = mid//F[i]
        count+=max(0,A[i]-a)
    if count <= K:
        right = mid
    else:
        left = mid
        
        

print(ans)
        
            

