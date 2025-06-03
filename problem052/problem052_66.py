n = input()
result = ""
for x in xrange(1,n+1):
    if x % 3 == 0:
        result = result + " " + str(x)

    elif x % 10 == 3:
        result = result + " " + str(x)

    else :
        i = x
        while i :
            i /= 10
            if i % 10 == 3:
                result = result + " " + str(x)
                break
print result