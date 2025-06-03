K = int(input())

if K%2 == 0 or K%5 == 0:
    print(-1)

elif K%7 == 0:
    x = -1
    b = 9*K/7
    c = 10%b

    for i in range(1,K+1):
        if c ==1:
            x = i
            break
        c = (c*10)%b

    print(x)

else:
    x = -1
    b = 9*K
    c = 10%b
    for i in range(1,K+1):
        if c ==1:
            x = i
            break
        c = (c*10)%b
        #print(c)
    print(x)