
X,Y = map(int,input().split())

key1 = Y - 2*X
key2 = 4*X - Y



if key1 % 2 != 0:
    print('No')
elif key2 % 2 != 0:
    print('No')
elif key1 < 0:
    print('No')
elif key2 < 0:
    print('No')
else:
    print('Yes')