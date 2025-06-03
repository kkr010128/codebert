a,v = map(int,input().split())
b,m = map(int,input().split())
n = int(input())

dis = abs(a-b)
a_move = n*v
b_move = n*m

if dis+b_move - a_move <= 0:
    print('YES')

else:
    print('NO')