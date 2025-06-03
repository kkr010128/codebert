s = int(input())
t = h = 0
for _ in range(s):
    tc, hc = input().split()
    if tc == hc:
        t += 1
        h += 1
    elif tc > hc :
        t += 3
    else:
        h += 3
print(t, h)