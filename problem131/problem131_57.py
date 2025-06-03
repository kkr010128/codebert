A,V = map(int,input().split())
B,W = map(int,input().split())
T = int(input())

w = abs(A-B)

if w <= (V-W)*T:
    print('YES')
else:
    print('NO')
