[H, N] = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

a = sum(A)
if H > a:
    print('No')
else:
    print('Yes')