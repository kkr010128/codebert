N,K = map(int,input().split())
A = list(map(int,input().split()))

left = 0
right = 10**9

while right - left > 1:
    center = (right+left)//2
    count = 0
    for a in A:
        if a%center == 0:
            count += a//center-1
        else:
            count += a//center
            
    if count >  K:
        left = center
    else:
        right = center
        
print(right)