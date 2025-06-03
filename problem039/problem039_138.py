a, b, c = [int(i) for i in input().split()]

if a < b:
    if b < c:
        print('Yes')
    else:
        print('No')
else:
    print('No')