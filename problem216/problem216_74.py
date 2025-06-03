A, B, C = [int(x) for x in input().split()]

if len({A, B, C}) == 2:
    print('Yes')
else:
    print('No')
