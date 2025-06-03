x, y = map(int, input().split())
l = max(x, y)
s = min(x, y)

for i in range(x):
    olds = s
    oldl = l
    s = oldl % olds
    l = olds

    if s == 0:
        print(l)
        break
