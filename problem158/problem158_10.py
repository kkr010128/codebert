k = int(input())
a, b = map(int, input().split())

if a % k != 0 and a // k == b // k:
    print('NG')
else:
    print('OK')
