k = int(input())
if k % 7 == 0:
    l = 9*k // 7
else:
    l = 9*k
if l % 2 == 0 or l % 5 == 0:
    print(-1)
else:
    pmo = 1
    for i in range(1, l + 1):
        mo = (pmo * 10) % l
        if mo == 1:
            print(i)
            break
        else:
            pmo = mo