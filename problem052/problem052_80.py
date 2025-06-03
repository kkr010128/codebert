n = int(input())
i = 1
ret = ""
while True:
    x = i
    if  x % 3 == 0:
        ret += " " + str(i)
    elif x % 10 == 3:
        ret += " " + str(i)
    else:
        x //= 10
        while x != 0:
            if x % 10 == 3:
                ret += " " + str(i)
                break
            x //= 10
    i+=1
    if i > n:
        break

print(ret)

