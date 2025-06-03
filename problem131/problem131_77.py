A, V = map(int,input().split())
B, W = map(int,input().split())
T = int(input())
if V!=W:
    t = (B-A)/(V-W)
    if A>B:
        t=-t
    if 0<=t<=T:
        print('YES')
    else:
        print('NO')
else:
    if A!=B:
        print('NO')
    else:
        print('YES')