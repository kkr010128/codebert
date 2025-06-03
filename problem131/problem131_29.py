A,V = map(int,input().split())
B,W = map(int,input().split())
T = int(input())
dif = abs(B-A)
speed = V-W
if speed <= 0:
    print('NO')
else:
    if speed*T >= dif:
        print('YES')
    else:
        print('NO')
