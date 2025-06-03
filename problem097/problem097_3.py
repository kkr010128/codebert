K = int(input())

if(7%K == 0):
    print(1)
else:
    mod = 7%K
    for i in range(2, K+1):
        if(mod * 10 + 7)%K == 0:
            print(i)
            break
        mod = (mod * 10 + 7)%K
    else:
        print(-1)