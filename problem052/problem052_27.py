n = input()

print '',
for i in xrange(1, n+1):
    x = i
    if x % 3 == 0:
        print i,
    else:
        while x:
            if x % 10 == 3:
                print i,
                break
            x /= 10