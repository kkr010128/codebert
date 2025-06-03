A,V = list(map(int, input().split()))
B,W = list(map(int, input().split()))
T = int(input())

if V-W > 0 and T*(V-W) >= abs(A-B):
    print('YES')
else:
    print('NO')