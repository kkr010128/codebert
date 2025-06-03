k = int(input())
a, b = map(int, input().split())

print('NG' if b // k == (a - 1) // k else 'OK')
