while True:
    num = raw_input()
    if num == "0":
        break
    output = 0
    for i in num:
        output += int(i)
    print output