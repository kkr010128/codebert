K = int(input())
if K % 2 == 0 or K % 5 == 0:
    print(-1)
else:
    i = 1
    r = 7 % K
    while(True):
        if r == 0:
            print(i)
            break
        r = (r * 10 + 7) % K
        i += 1
