while True:
    x = input()
    if x == "0":
        break
    x = list(map(int, list(x)))
    print(sum(x))

