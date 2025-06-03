k = int(input())
a, b = map(int, input().split())

n = a // k

if k * n == a:
    print('OK')
elif k * (n + 1) <= b:
    print('OK')
else:
    print('NG')