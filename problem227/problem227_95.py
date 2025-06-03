N,K = (int(x) for x in input().split())
H   = sorted([int(x) for x in input().split()])
if K>=len(H):
    print('0')
else:
    print(sum(H[:len(H)-K]))