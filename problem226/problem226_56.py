H,N = (int(x) for x in input().split())
A   = [int(x) for x in input().split()]
if sum(A)>=H:
    print('Yes')
else:
    print('No')