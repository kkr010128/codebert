n = int(input())
for cnt in range(n):
    t = list(map(int, input().split()))
    t.sort()
    if t[2]**2 == t[1]**2 + t[0]**2:
        print('YES')
    else:
        print('NO')