A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

if W>=V:
    print('NO')
    exit()
if abs(A-B)/(V-W) > T:
    print('NO')
    exit()

print('YES')