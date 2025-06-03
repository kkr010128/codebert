while (True):
    s = list(map(int, input().strip().split(' ')))

    if s[0] == 0 and s[1] == 0:
        break
    else:
        for i in range(s[0]):
            for j in range(s[1]):
                if j % 2 == 0 and i % 2 == 0:
                    print("#", end="")
                elif j % 2 == 1 and i % 2 == 0:
                    print(".", end="")
                elif j % 2 == 0 and i % 2 == 1:
                    print(".",end="")
                else:
                    print("#", end="")
            print()
    print()
