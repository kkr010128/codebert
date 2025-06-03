n = int(input())
a = list(map(int, input().split()))

pm = sum(a)
e = 1
te = 1
for i in a:
    pm -= i
    e = min((e-i)*2, pm)
    if e < 0:
        break
    te += e
if e < 0:
    print(-1)
else:
    print(te)