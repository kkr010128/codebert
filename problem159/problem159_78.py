X = int(input())

K = 100
i = 1
while 1:
    K *= 101
    K //= 100
    if K >= X:
        break
    i += 1
print(i)