while True:
    i = list(map(int, input().split()))
    if i[0] == 0 and i[1] == 0:
        break
    else:
        for j in range(i[0]):
            for k in range(i[1]):
                if j % 2 == 0 and k % 2 == 0:
                    print("#", end='')
                elif j % 2 == 1 and k % 2 == 1:
                    print("#", end='')
                else:
                    print(".", end='')
            print("\n", end='')
        print("\n", end='')
