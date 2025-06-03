s = int(input())

for x in range(s):
    r = sorted(list(map(int, input().split())))
    if r[2] ** 2 == r[0] ** 2 + r[1] ** 2:
        print('YES')
    else:
        print('NO')

