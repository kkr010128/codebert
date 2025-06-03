while True:
    ans = 0
    x = raw_input()
    if x == "0":
        break
    for i in x:
        ans += int(i)
    print ans