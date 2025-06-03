x, n = map(int, input().split())
p = list(map(int,input().split()))
if x not in p:
    y = x
else:
    i = 1
    y = x
    while y == x:
        if x - i not in p:
            y = x - i
        elif x + i not in p:
            y = x + i
        i += 1
print(y)