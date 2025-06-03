while True:
    data = input()
    if(data == "-"):break
    m = int(input())
    tmp = []

    for i in range(m):
        num = int(input())
        if(len(tmp) == 0):
            tmp = data[num:] + data[:num]
            data = ""
        else:
            data = tmp[num:] + tmp[:num]
            tmp = ""
    if(data): print(data)
    else: print(tmp)
