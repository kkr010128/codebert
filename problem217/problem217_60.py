_ = input()
l = list(map(int, input().split(' ')))
print('APPROVED' if all([(a % 2 == 1 or a % 3 == 0 or a % 5 == 0) for a in l]) else 'DENIED')
