def func(l):
    i = 0
    for num in range(l[0], l[1]+1):
        #print(num)
        if l[2] % num == 0:
            #print(num)
            i = i + 1
    return i

if __name__ == '__main__':
    N = input().split(" ")
    l = []
    for i in N:
        l.append(int(i))

    result = func(l)
    print(result)