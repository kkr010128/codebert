while True:
    x = input()
    if x == "0":
        break
    num = [int(i) for i in x]
    print(sum(num))