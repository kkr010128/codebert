k = int(input())
s = 7
num = 1
res = True
if k == 2:
    print(-1)
else:
    for i in range(k):
        s %= k
        if s == 0:
            res = False
            print(num)
            break
        num += 1
        s *= 10
        s += 7
    if res:
        print(-1)