A, V = [int(x) for x in input().split()]
B, W = [int(x) for x in input().split()]
T = int(input())

if W >= V:
    print('NO')
elif abs(A - B) <= (V - W) * T:
    print('YES')
else:
    print('NO')