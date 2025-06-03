#a = list(map(int, input().split(' ')))
a = input()
b = input()

if a == b[:-1]:
    print('Yes')
else:
    print('No')