import sys
i = input().split()

a,b,c = int(i[0]),int(i[1]),int(i[2])

if a >= b:
    print('No')
    sys.exit()
elif b < c:
    print('Yes')
    sys.exit()
else:
    print('No')
