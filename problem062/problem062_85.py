x = input()
while 1:
    sum_x = 0
    if x == "0":
        break
    for c in x:
        sum_x += int(c)
    print(sum_x)
    x = input()