X, Y = map(int, input().split())
for i in range(100):
    j = X - i
    if j < 0:
        continue
    if 2 * i + 4 * j == Y:
        print('Yes')
        break
else:
    print('No')
