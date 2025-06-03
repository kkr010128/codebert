N=int(input())
for line in range(N):
    a,b,c = (int(i) for i in input().split())
    if (a**2+b**2==c**2) or (b**2+c**2==a**2) or (c**2+a**2==b**2):
        print('YES')
    else:
        print('NO')