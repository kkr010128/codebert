K = int(input())
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(K):
    t = l[i] % 10
    if t == 0:
        l.append(l[i] * 10 + 0)
        l.append(l[i] * 10 + 1)
    elif t == 9:
        l.append(l[i] * 10 + 8)
        l.append(l[i] * 10 + 9)
    else:
        l.append(l[i] * 10 + t - 1)
        l.append(l[i] * 10 + t)
        l.append(l[i] * 10 + t + 1)

print(l[K-1])