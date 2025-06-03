x, y = map(int, input().split())
s = [400000, 300000, 200000, 100000]

if x == 1 and y == 1:
    print(sum(s))
elif x <= 3 and y <= 3:
    print(s[x] + s[y])
elif x <= 3:
    print(s[x])
elif y <= 3:
    print(s[y])
else:
    print(0)