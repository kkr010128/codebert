a,b=map(int,input().split())
c,d=map(int,input().split())
t=int(input())
if abs(a-c)<=(b-d)*t:
    print('YES')
else:
    print('NO')
