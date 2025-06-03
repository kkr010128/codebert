while True:
    n = input()
    if n == "0":
        break
    ans = sum([int(x) for x in n])
    print(ans)