def resolve():
    K = int(input())
    lunluns = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    count = 9
    pointer = 0
    while K > count:
        lunnum = lunluns[pointer]
        lunlast = int(str(lunnum)[-1])
        if lunlast == 0:
            for i in [0, 1]:
                lunluns.append(int(str(lunnum)+str(lunlast+i)))
                count += 1
        elif lunlast == 9:
            for i in [-1, 0]:
                lunluns.append(int(str(lunnum)+str(lunlast+i)))
                count += 1
        else:
            for i in [-1, 0, 1]:
                lunluns.append(int(str(lunnum)+str(lunlast+i)))
                count += 1
        pointer += 1
    print(lunluns[K-1])

if '__main__' == __name__:
    resolve()