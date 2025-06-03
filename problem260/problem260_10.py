ls = list(map(int, input().split(' ')))
if sum(ls) >= 22:
    print('bust')
else:
    print('win')