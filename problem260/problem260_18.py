a = list(map(int, input().split()))
suma = a[0] + a[1] + a[2]
if suma >= 22:
    print('bust')
else:
    print('win')