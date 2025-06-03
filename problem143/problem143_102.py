k = int(input())
s = input()

if len(s)>k:
    print('{}...'.format(s[:k]))
else:
    print(s)