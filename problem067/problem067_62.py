n = int(input())
t = 0
h = 0
for i in range(n):
    taro,hana = input().split()
    if taro == hana:
        t += 1
        h += 1
    else:
        m = list((taro,hana))
        m.sort()
        if m == list((taro,hana)):
            h += 3
        else:
            t += 3
print("{} {}".format(t,h))