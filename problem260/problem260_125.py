a = list(map(int, input().split()))
sum_a = sum(a)
if sum_a >= 22:
    print('bust')
else:
    print('win')