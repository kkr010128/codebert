while True:
    num = input()
    if(num == "0"): break
    ret = 0
    for i in num:
        ret += int(i)
    print(ret)
