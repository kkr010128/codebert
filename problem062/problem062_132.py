while 1:
    num = input()
    if num == "0":
        break

    a = []
    for i in range(len(num)):
        a.append(int(num[i:i+1]))
    print(sum(a))