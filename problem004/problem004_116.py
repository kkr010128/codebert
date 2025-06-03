N = int(input())
for i in range(N):
    a, b, c = map(int, input().split())
    a2 = a ** 2
    b2 = b ** 2
    c2 = c ** 2
    if a2 + b2 == c2 or a2 + c2 == b2 or b2 + c2 == a2:
        print('YES')
    else:
        print('NO')