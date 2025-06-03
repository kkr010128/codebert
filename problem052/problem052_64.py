n = int(raw_input())
s = ''
for i in range(1,n+1):
    if (i % 3) == 0:
        s = s + ' ' + str(i)
    else:
        x = i
        while True:
            if (x % 10) == 3:
                s = s + ' ' + str(i)
                break
            x = x / 10
            if x == 0:
                break
print s