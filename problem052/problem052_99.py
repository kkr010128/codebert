def check3(m):
    m = str(m)
    if '3' in m:
        return True
    else:
        return False

n = int(input())

i = 1


while i <= n:
    x = i
    if x%3 == 0 or x%10 == 3:
        print(" %d" % i, end = '')
        i += 1
    else:
        isThree = check3(x)
        if isThree:
            print(" %d" % i, end = '')
        i += 1
print("")