n = int(input())
for i in range(n):
    a = sorted(map(int, input().split()))
    print('YES' if a[0] ** 2 + a[1] ** 2 == a[2] ** 2 else 'NO')