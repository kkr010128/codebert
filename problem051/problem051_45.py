from itertools import cycle

while True:
    (H, W) = [int(i) for i in input().split(' ')]
    if (H == W == 0):
        break

    it1 = cycle(['#', '.'])
    it2 = cycle(['.', '#'])

    str1 = ''
    str2 = ''

    for i in range(W):
        str1 += next(it1)
        str2 += next(it2)

    for i in range(H):
        if ((i % 2) == 0):
            print(str1)
        else:
            print(str2)

    print()