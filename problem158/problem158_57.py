k = int(input())
a, b = map(int, input().split())
for n in range(a, b+1):
    if n % k == 0:
        print('OK')
        break
    if n == b:
        print('NG')