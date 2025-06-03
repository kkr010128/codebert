from collections import defaultdict

d = defaultdict(lambda: 0)

N = int(input())

for _ in range(N):
    ord, str = input().split()
    if ord == 'insert':
        d[str] = 1
    else:
        if str in d:
            print('yes')
        else:
            print('no')