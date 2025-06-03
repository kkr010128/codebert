n=int(raw_input())
i = 1
print "",
while(i<=n):
    x=i
    if x%3 is 0:
        print i,
    else:
        for j in xrange(0,4):
            if (x/10**j)%10 is 3:
                print i,
                break
    i = i+1