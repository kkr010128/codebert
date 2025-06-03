k = int(input())
a, b = map(int, input().split())

range_max = int(b / k) * k
if range_max >= a:
    print('OK')
else:
    print('NG')
