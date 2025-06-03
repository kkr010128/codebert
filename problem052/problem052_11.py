n = input()
array = []
i = 1
while i <= n:
    x = i
    if x % 3 == 0:
        array.append(i)
    else:
        while x != 0:
            if x % 10 == 3:
                array.append(i)
                break
            x /= 10
    i += 1
print str(array).replace('[', ' ').replace(']', '').replace(',', '')