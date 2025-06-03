a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())
if a <= b:
    total_a = a + v * t
    total_b = b + w * t
    if total_a >= total_b:
        print('YES')
    else:
        print('NO')
else:
    total_a = a - v * t
    total_b = b - w * t
    if total_a <= total_b:
        print('YES')
    else:
        print('NO')