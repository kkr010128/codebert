[a,b,c] = list(map(int,input().split()))

if c-a-b<0:
    print('No')
else:
    left = 4*a*b
    right = (c-a-b)**2
    if left<right:
        print('Yes')
    else:
        print('No')