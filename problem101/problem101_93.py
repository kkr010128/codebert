a,b,c = map(int,input().split())
k = int(input())

for i in range(k):
    if a >= b:
        b *= 2
    elif b >= c:
        c *= 2
    else:
        pass

if a < b and b < c:
    print('Yes')
else:
    print('No')