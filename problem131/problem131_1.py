import sys
a = list(map(int,input().split()))
b = list(map(int,input().split()))
t = int(input())
if a[1] <= b[1]:
    print('NO')
    sys.exit()
elif abs(a[0]-b[0])/abs(a[1]-b[1]) <= t:
    print('YES')
    sys.exit()
else:
    print('NO')