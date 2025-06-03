while True:
    x = list(input())
    if x[0] == "0":
        break
    sum = 0
    for i in range(len(x)):
        sum += int(x[i])
    print(sum)
    #print(x)