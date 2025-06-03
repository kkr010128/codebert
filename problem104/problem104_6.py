l, r, d = map(int, input().split())
c = 0
x = (l // d) + 1
if(l % d == 0):
    c = 1
while(True):
    m = d * x
    x += 1
    if(m <= r):
        c += 1
    else:   break
print(c)