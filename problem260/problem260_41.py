a1,a2,a3 = map(int,input().split())

sum = a1
sum += a2
sum += a3

if sum <=21:
    print('win')
else:
    print('bust')
