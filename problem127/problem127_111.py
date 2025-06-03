X, Y = map(int, input().split(' '))
print('Yes' if (X * 2 <= Y <= X * 4) and (Y % 2 == 0) else 'No')
