a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())

d = abs(a-b)
if v <= w:
    print('NO')
else:
    if (v-w)*t < d:
        print('NO')
    else:
        print('YES')
