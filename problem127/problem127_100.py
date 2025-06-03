x,y = map(int,input().split())
if y % 2 != 0:
    print('No')
elif x * 2 <= y <= x * 4:
    print('Yes')
else:
    print('No')