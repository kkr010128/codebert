n = int(input())
dat = []
for _ in range(n):
    x, l =map(int, input().split())
    dat.append([x-l, x+l])
dat.sort(key=lambda x: x[1])
#print(dat)
prevr = -99999999999999999
res = 0
for i in range(n):
    if dat[i][0] >= prevr:
        prevr = dat[i][1]
        res += 1
print(res)

