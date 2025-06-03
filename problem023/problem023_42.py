import collections

hoge = collections.defaultdict(lambda: 'no')
num = int(input())

for _ in range(num):
    command, key = input().split()
    if command == 'insert':
        hoge[key] = 'yes'
    else:
        print(hoge[key])
