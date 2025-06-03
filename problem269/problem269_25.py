import sys
read = sys.stdin.read

T1, T2, A1, A2, B1, B2 = map(int, read().split())
answer = 0
v1 = A1 - B1
v2 = A2 - B2
d = v1 * T1 + v2 * T2

if d == 0:
    print('infinity')
    exit()
elif v1 * d > 0:
    print(0)
    exit()

if v1 * T1 % -d == 0:
    print(v1 * T1 // -d * 2)
else:
    print(v1 * T1 // -d * 2 + 1)