k = int(input())

a, b = map(int, input().split())

if a <= k <= b or k <= b/2:
    print('OK')

else:
    print('NG')
