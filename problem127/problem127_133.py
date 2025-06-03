X,Y = map(int, input().split())

if 4*X < Y or Y < 2*X or Y%2 != 0:
    print('No')
    exit()

print('Yes')