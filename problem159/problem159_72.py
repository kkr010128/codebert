X = int(input())

c = 0
i = 100
while True:
    c += 1
    i = i + i//100
    if  X <= i:
        break
print(c)