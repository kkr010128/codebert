while True:
    a, b = map(int, input().split())
    if a or b:
        for i in range(0, a):
            for j in range(0, b):
                print("#", end = '')
            print()
        print()
    else:
        break
