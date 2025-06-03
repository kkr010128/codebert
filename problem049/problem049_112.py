while True:
    x = input().split()
    x_int = [int(i) for i in x]

    if x_int[0] == 0 and x_int[1] ==0:
        break
    for i in range(x_int[0]):
        z = '#' * x_int[1]
        print(z)
    print()