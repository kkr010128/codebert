def five_variables():
    x = list(map(int, input().split()))
    for i, j in enumerate(x):
        if j == 0:
            print(i+1)
            break

five_variables()