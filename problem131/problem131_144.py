A,V = [int(i) for i in input().split()]
B,W = [int(i) for i in input().split()]
T = int(input())

if A < B:
    if A+V*T >= B+W*T:
        print('YES')
    else:
        print('NO')
else:
    if A-V*T <= B-W*T:
        print('YES')
    else:
        print('NO')
