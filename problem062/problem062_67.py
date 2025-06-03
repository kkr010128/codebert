while True:
    num = input()
    if int(num) == 0:
        break
    sum = 0
    for i in num:
        a = int(i)
        sum += a
    print(sum)
