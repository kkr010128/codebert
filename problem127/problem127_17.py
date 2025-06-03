X, Y = map(int, input().split())

for i in range(X + 1):
    tsuru = i
    kame = X - i
    if tsuru * 2 + kame * 4 == Y:
        print('Yes')
        exit()
print('No')
